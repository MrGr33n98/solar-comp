import reflex as rx
from sqlmodel import Session, select
from typing import Optional
import bcrypt

from ..models.user import User
from ..models.company import Company

class AuthState(rx.State):
    """Estado para gerenciar autenticação e estado do usuário."""
    
    # Estado do usuário
    user_id: Optional[str] = None
    user_email: Optional[str] = None
    user_name: Optional[str] = None
    user_type: Optional[str] = None
    is_authenticated: bool = False
    login_error: Optional[str] = None
    
    # Estado do formulário
    email: str = ""
    password: str = ""
    confirm_password: str = ""
    full_name: str = ""
    form_error: Optional[str] = None
    
    def login(self) -> bool:
        """Realiza o login do usuário usando os dados do estado."""
        with Session(self.app.db_engine) as session:
            user = session.exec(
                select(User).where(User.email == self.email)
            ).first()
            
            if not user:
                self.login_error = "Usuário não encontrado"
                return False

            if not bcrypt.checkpw(self.password.encode(), user.hashed_password.encode()):
                self.login_error = "Senha incorreta"
                return False
            
            # Login bem sucedido
            self.user_id = str(user.id)
            self.user_email = user.email
            self.user_name = user.full_name
            self.user_type = user.user_type
            self.is_authenticated = True
            self.login_error = None
            return True
    
    def logout(self):
        """Realiza o logout do usuário."""
        self.user_id = None
        self.user_email = None
        self.user_type = None
        self.is_authenticated = False
    
    def register(self, user_type: str = "consumer") -> bool:
        """Registra um novo usuário utilizando os dados do formulário."""
        if self.password != self.confirm_password:
            self.form_error = "As senhas não coincidem"
            return False

        with Session(self.app.db_engine) as session:
            # Verifica se email já existe
            existing_user = session.exec(
                select(User).where(User.email == self.email)
            ).first()
            
            if existing_user:
                self.form_error = "Email já cadastrado"
                return False
            
            # Cria novo usuário
            hashed_password = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt()).decode()
            new_user = User(
                email=self.email,
                hashed_password=hashed_password,
                full_name=self.full_name,
                user_type=user_type
            )
            
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            
            # Auto-login após registro
            self.user_id = str(new_user.id)
            self.user_email = new_user.email
            self.user_name = new_user.full_name
            self.user_type = new_user.user_type
            self.is_authenticated = True
            self.login_error = None
            self.form_error = None
            return True

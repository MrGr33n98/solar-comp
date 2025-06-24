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
    
    # Estado do formulário
    email: str = ""
    password: str = ""
    confirm_password: str = ""
    full_name: str = ""
    form_error: Optional[str] = None
    
    def login(self, email: str, password: str) -> bool:
        """Realiza o login do usuário."""
        with Session(self.app.engine) as session:
            user = session.exec(
                select(User).where(User.email == email)
            ).first()
            
            if not user:
                self.login_error = "Usuário não encontrado"
                return False
            
            if not bcrypt.checkpw(password.encode(), user.hashed_password.encode()):
                self.login_error = "Senha incorreta"
                return False
            
            # Login bem sucedido
            self.user_id = str(user.id)
            self.user_email = user.email
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
    
    def register(self, email: str, password: str, full_name: str, user_type: str = "consumer") -> bool:
        """Registra um novo usuário."""
        with Session(self.app.engine) as session:
            # Verifica se email já existe
            existing_user = session.exec(
                select(User).where(User.email == email)
            ).first()
            
            if existing_user:
                self.login_error = "Email já cadastrado"
                return False
            
            # Cria novo usuário
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_user = User(
                email=email,
                hashed_password=hashed_password,
                full_name=full_name,
                user_type=user_type
            )
            
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            
            # Auto-login após registro
            self.user_id = str(new_user.id)
            self.user_email = new_user.email
            self.user_type = new_user.user_type
            self.is_authenticated = True
            return True

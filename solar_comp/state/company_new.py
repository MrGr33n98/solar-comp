"""Estado para gerenciar empresas e marketplace."""

import reflex as rx
from sqlmodel import Session, select
from typing import List, Optional, Dict, Any
from datetime import datetime

from ..models.company import Company, CompanyService, CompanyProject
from ..models.marketplace import Review, Lead


class CompanyState(rx.State):
    """Estado para gerenciar operações de empresas."""

    # Estado das empresas
    companies: List[Dict[str, Any]] = []
    selected_company: Optional[Dict[str, Any]] = None
    loading: bool = False

    # Filtros de busca
    search_query: str = ""
    selected_city: str = ""
    min_rating: str = "0"  # Usando string para compatibilidade com select

    # Formulário de empresa
    company_name: str = ""
    company_description: str = ""
    company_cnpj: str = ""
    company_address: str = ""
    company_city: str = ""
    company_state: str = ""
    company_phone: str = ""
    company_email: str = ""
    company_website: str = ""
    form_error: Optional[str] = None

    def load_companies(self):
        """Carrega lista de empresas ativas."""
        self.loading = True
        with Session(self.app.db_engine) as session:
            companies = session.exec(
                select(Company).where(Company.is_active == True)
            ).all()
            
            self.companies = [
                {
                    "id": str(company.id),
                    "name": company.name,
                    "description": company.description or "",
                    "city": company.city,
                    "state": company.state,
                    "average_rating": company.average_rating,
                    "total_reviews": company.total_reviews,
                    "phone": company.phone or "",
                    "email": company.email or "",
                    "website": company.website or "",
                    "is_verified": company.is_verified,
                }
                for company in companies
            ]
        self.loading = False

    def filter_companies(self) -> List[Dict[str, Any]]:
        """Filtra empresas baseado nos critérios de busca."""
        filtered = self.companies
        
        if self.search_query:
            query = self.search_query.lower()
            filtered = [
                company for company in filtered
                if query in company["name"].lower() 
                or query in company["description"].lower()
            ]
        
        if self.selected_city:
            filtered = [
                company for company in filtered
                if company["city"].lower() == self.selected_city.lower()
            ]
        
        try:
            min_rating = float(self.min_rating)
            if min_rating > 0:
                filtered = [
                    company for company in filtered
                    if company["average_rating"] >= min_rating
                ]
        except (ValueError, TypeError):
            pass  # Ignora se não for um número válido
        
        return filtered

    def register_company(self):
        """Registra uma nova empresa."""
        # Validações
        if not all([
            self.company_name,
            self.company_cnpj,
            self.company_city,
            self.company_state
        ]):
            self.form_error = "Por favor, preencha todos os campos obrigatórios"
            return
        
        if len(self.company_cnpj) != 14:
            self.form_error = "CNPJ deve ter 14 dígitos"
            return
        
        with Session(self.app.db_engine) as session:
            # Verificar se CNPJ já existe
            existing = session.exec(
                select(Company).where(Company.cnpj == self.company_cnpj)
            ).first()
            
            if existing:
                self.form_error = "CNPJ já cadastrado"
                return
            
            # Criar nova empresa
            new_company = Company(
                name=self.company_name,
                description=self.company_description,
                cnpj=self.company_cnpj,
                address=self.company_address,
                city=self.company_city,
                state=self.company_state,
                phone=self.company_phone,
                email=self.company_email,
                website=self.company_website,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
            
            try:
                session.add(new_company)
                session.commit()
                session.refresh(new_company)
                
                # Limpar formulário
                self._clear_form()
                self.form_error = None
                
                # Recarregar lista
                self.load_companies()
                
                return rx.redirect("/empresas")
            
            except Exception as e:
                self.form_error = "Erro ao cadastrar empresa. Tente novamente."
                session.rollback()

    def _clear_form(self):
        """Limpa os campos do formulário."""
        self.company_name = ""
        self.company_description = ""
        self.company_cnpj = ""
        self.company_address = ""
        self.company_city = ""
        self.company_state = ""
        self.company_phone = ""
        self.company_email = ""
        self.company_website = ""


class LeadState(rx.State):
    """Estado para gerenciar leads/contatos."""
    
    # Formulário de contato
    lead_name: str = ""
    lead_email: str = ""
    lead_phone: str = ""
    lead_message: str = ""
    selected_company_id: Optional[str] = None
    form_error: Optional[str] = None
    form_success: bool = False

    def send_lead(self):
        """Envia um lead para uma empresa."""
        if not all([
            self.lead_name,
            self.lead_email,
            self.lead_message,
            self.selected_company_id
        ]):
            self.form_error = "Por favor, preencha todos os campos obrigatórios"
            return
        
        with Session(self.app.db_engine) as session:
            # Verificar se empresa existe
            company = session.exec(
                select(Company).where(Company.id == self.selected_company_id)
            ).first()
            
            if not company:
                self.form_error = "Empresa não encontrada"
                return
            
            # Criar novo lead
            new_lead = Lead(
                company_id=self.selected_company_id,
                name=self.lead_name,
                email=self.lead_email,
                phone=self.lead_phone,
                message=self.lead_message,
                created_at=datetime.now(),
            )
            
            try:
                session.add(new_lead)
                session.commit()
                
                # Limpar formulário e mostrar sucesso
                self._clear_lead_form()
                self.form_success = True
                self.form_error = None
            
            except Exception as e:
                self.form_error = "Erro ao enviar mensagem. Tente novamente."
                session.rollback()

    def _clear_lead_form(self):
        """Limpa o formulário de lead."""
        self.lead_name = ""
        self.lead_email = ""
        self.lead_phone = ""
        self.lead_message = ""
        self.form_success = False

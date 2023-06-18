from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship, registry, declarative_base
from sqlalchemy.sql import func
from sqlalchemy import String, Integer, Column, DateTime, ForeignKey
from .connection import engine
from ..modules.cryptopass import generate_pass, decode_pass
from .via_cep import Via_cep
import datetime

DBase = declarative_base()
reg = registry()

class Base(DBase):
     __tablename__ = 'tb_bases'

     base_id: Mapped[int] = mapped_column(primary_key=True)
     base_nome: Mapped[str] = mapped_column(String(30), nullable=False)
     base_desc: Mapped[str] = mapped_column(String(300))

     def __repr__(self) -> str:
          return f"Base -> (base_id={self.base_id!r}, base_nome={self.base_nome!r}, base_desc={self.base_desc!r})"

class Cargo(DBase):
     __tablename__ = 'tb_cargos'

     cargo_id: Mapped[int] = mapped_column(primary_key=True)
     cargo_nome: Mapped[str] = mapped_column(String(30), nullable=False)
     cargo_desc: Mapped[str] = mapped_column(String(300))

     def __repr__(self) -> str:
          return f"Cargo -> (cargo_id={self.cago_id!r}, cargo_nome={self.cargo_nome!r}, cargo_desc={self.cargo_desc!r})"

class Colaborador(DBase):
     __tablename__ = 'tb_colaboradores'

     registro = Column(DateTime(timezone=True), server_default=func.now())
     colab_id: Mapped[int] = mapped_column(Integer, primary_key=True)
     colab_matricula: Mapped[Optional[int]]
     colab_nome: Mapped[str] = mapped_column(String(50), nullable=False)
     colab_nascimento: Mapped[Optional[datetime.date]]
     colab_cpf: Mapped[str] = mapped_column(String(11), nullable=False)
     colab_rg: Mapped[str] = mapped_column(String(9), nullable=True)
     colab_est_civil: Mapped[str] = mapped_column(String(15), nullable=True)
     colab_naturalidade: Mapped[str] = mapped_column(String(30), nullable=True)
     end_id: Mapped[Optional[int]]
     colab_fone: Mapped[str] = mapped_column(String(13), nullable=True)
     colab_celular: Mapped[str] = mapped_column(String(14), nullable=True)
     colab_escolaridade: Mapped[str] = mapped_column(String(50), nullable=True)
     cargo_id: Mapped[Optional[int]]
     colab_admissao: Mapped[Optional[datetime.date]]
     colab_email: Mapped[str] = mapped_column(String(100), nullable=True)
     colab_centro_custo: Mapped[str] = mapped_column(String(100), nullable=True)
     colab_salario: Mapped[Optional[float]]
     colab_status: Mapped[bool]
     base_id: Mapped[Optional[int]]
     colab_login: Mapped[str] = mapped_column(String(50), nullable=False)
     colab_password: Mapped[str] = mapped_column(String(100), nullable=True)

     def __init__(self, colab_matricula:int, colab_nome:str, colab_cpf:str, colab_login:str, colab_password:str):
          self.colab_matricula = colab_matricula
          self.colab_nome = colab_nome
          self.colab_cpf = colab_cpf
          self.colab_login = colab_login
          self.colab_password = self.__generate_hash(colab_password)
          self.colab_status = False

     def __repr__(self) -> str:
          return f"Colaborador -> (colab_id={self.colab_id!r}, colab_nome={self.colab_nome!r})"

     def __generate_hash(self, password):
          return generate_pass(password)

class Endereco(DBase):
     __tablename__ = 'tb_enderecos'

     end_id: Mapped[int] = mapped_column(primary_key=True)
     end_tipo: Mapped[str] = mapped_column(String(1), nullable=False)
     end_cep: Mapped[Optional[int]]
     end_logradouro: Mapped[Optional[str]] = mapped_column(String(100))
     end_numero: Mapped[Optional[int]]
     end_bairro: Mapped[Optional[str]] = mapped_column(String(100))
     end_cidade: Mapped[Optional[str]] = mapped_column(String(100))
     end_uf: Mapped[Optional[str]] = mapped_column(String(2))
     end_referencia: Mapped[Optional[str]] = mapped_column(String(300))

     def __init__(self, end_tipo:str, end_cep:int, end_numero:int, end_referencia:str):
          self.end_cep = end_cep
          self.end_tipo = end_tipo
          self.end_numero = end_numero
          self.end_referencia = end_referencia

     def __repr__(self) -> str:
          return f"Endereco -> (end_id={self.end_id!r}, end_cep={self.end_cep!r}, end_logradouro={self.end_logradouro!r}, end_numero={self.end_numero!r}, end_bairro={self.end_bairro!r}, end_cidade={self.end_cidade!r}, end_uf={self.end_uf!r}, end_referencia={self.end_referencia!r})"
     
     def get_end_from_viacep(self) -> dict:
          via_cep = Via_cep(self.end_cep)
          end = via_cep.get_end()
          self.set_end_from_viacep(end)
          return end
     
     def set_end_from_viacep(self, data:dict) -> None:
          self.end_logradouro = data['logradouro']
          self.end_bairro = data['bairro']
          self.end_cidade = data['localidade']
          self.end_uf = data['uf']
     
DBase.metadata.create_all(engine)
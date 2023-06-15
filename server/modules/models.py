from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship, registry, declarative_base
from sqlalchemy.sql import func
from sqlalchemy import String, Integer, Column, DateTime, ForeignKey
from .connection import engine
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
     colab_senha: Mapped[str] = mapped_column(String(100), nullable=True)

     def __repr__(self) -> str:
          return f"Colaborador -> (colab_id={self.colab_id!r}, colab_nome={self.colab_nome!r})"
     
     def __generate_hash(self):
          self.senha_hash = "Myhash"

DBase.metadata.create_all(engine)
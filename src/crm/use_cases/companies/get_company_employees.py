from typing import Dict, Any, List, Optional

from src.crm.domain.entities.employees import EmployeeEntity
from src.crm.domain.interfaces.daos.companies import ICompaniesDAO
from src.crm.domain.interfaces.daos.emopoyees import IEmployeesDAO


class GetCompanyEmployees:
    def __init__(
            self,
            company_dao: ICompaniesDAO,
            employee_dao: IEmployeesDAO
    ):
        self._company_dao = company_dao
        self._employee_dao = employee_dao

    async def execute(
            self,
            company_id: int,
            role: Optional[str] = None,
            min_salary: Optional[int] = None,
            max_salary: Optional[int] = None,
            is_manager: Optional[bool] = None,
            status: Optional[str] = None
    ) -> Dict[str, Any]:
        employees: List[EmployeeEntity] = await self._employee_dao.list_filtered(
            company_id=company_id,
            role=role,
            min_salary=min_salary,
            max_salary=max_salary,
            is_manager=is_manager,
            status=status
        )
        all_role_counts: Dict[str, int] = await self._employee_dao.count_by_role(company_id)

        outed_role_counts: Dict[str, int] = {}
        for employee in employees:
            outed_role_counts[employee.role] = outed_role_counts.get(employee.role, 0) + 1

        return {
            "employees": [emp.to_dict() for emp in employees],
            "all_role_counts": all_role_counts,
            "outed_role_counts": outed_role_counts
        }

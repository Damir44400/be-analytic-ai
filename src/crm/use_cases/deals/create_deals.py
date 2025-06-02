from src.crm.domain.entities.deals import DealEntity
from src.crm.domain.exceptions import BadRequestException
from src.crm.domain.interfaces.daos.deals import ICreateDealDAO
from src.crm.domain.interfaces.daos.emopoyees import IEmployeeGetByUserCompanyDAO
from src.crm.domain.interfaces.uow import IUoW


class DealGateway(ICreateDealDAO):
    ...


class CreateDeals:
    def __init__(
            self,
            uow: IUoW,
            deal_gateway: DealGateway,
            employee_gateway: IEmployeeGetByUserCompanyDAO
    ):
        self._uow = uow
        self._deal_gateway = deal_gateway
        self._employee_gateway = employee_gateway

    async def execute(
            self,
            deal: DealEntity,
            user_id: int
    ) -> DealEntity:
        employee = await self._employee_gateway.get_by_user_and_company(
            user_id,
            deal.company_id
        )

        if not employee:
            raise BadRequestException("You do not have an employee to create this deal")

        async with self._uow:
            return await self._deal_gateway.create(deal)

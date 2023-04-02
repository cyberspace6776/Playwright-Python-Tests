from api_body import bodyForBP, bodyForCountry, bodyForLocation, createHeaders


class ApiIndicatorMessage:

    def __init__(self, api_request_context) -> None:
        self.api_request_context = api_request_context

    async def create_body(self, imtype, indicator_id, affected):
        if (imtype == 'country'):
            return await bodyForCountry(affected, indicator_id)
        elif (imtype == 'location'):
            return await bodyForLocation(affected, indicator_id)
        elif (imtype == 'business_partner'):
            return await bodyForBP(affected, indicator_id)

    async def create_message(self, user_token: str, imtype, indicator_id: str, affected):
        response = await self.api_request_context.post(
            url=f"/v2/indicator_messages/{imtype}",
            headers=await createHeaders(user_token),
            data=await self.create_body(imtype, indicator_id, affected),
        )
        return response

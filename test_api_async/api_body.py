from faker import Faker

fake = Faker()
messageBody = fake.sentence()
valid_until = "2023-03-24T12:00:00"


async def createHeaders(userToken: str):
    header = {
        'Authorization': f'Bearer {userToken}',
        'Content_type': 'application/vnd.api+json',
        'Accept': 'application/vnd.api+json',
    }
    return header


async def bodyForCountry(country: str, indicator_id):
    body = {
        'data': {
            'type': 'indicator_message',
            'attributes': {
                'subject': 'Country Incident test',
                'body': messageBody,
                'source': 'Riskmethods',
                'score': 100,
                'valid_until': valid_until,
                'country_id': country
            },
            'relationships': {
                'indicator': {
                    'data': {
                        'type': 'indicator',
                        'id': indicator_id
                    }
                }
            }
        }
    }
    return body


def bodyForBP(roId, indicatorId):
    body = {
        'data': {
            'type': 'indicator_message',
            'attributes': {
                'subject': 'Business Partner Incident test',
                'body': messageBody,
                'source': 'Riskmethods',
                'score': 100,
                'valid_until': valid_until,
                'business_partner_ids': [roId]
            },
            'relationships': {
                'indicator': {
                    'data': {
                        'type': 'indicator',
                        'id': indicatorId
                    }
                }
            }
        }
    }
    return body


def bodyForLocation(supplier: dict, indicatorId):
    body = {
        'data': {
            'type': 'indicator_message',
            'attributes': {
                'subject': 'Location Incident test',
                'body': messageBody,
                'source': 'Riskmethods',
                'score': 100,
                'valid_until': valid_until,
                'locations': [
                    {
                        'type': 'circle',
                        'radius': 0,
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [
                                supplier["lng"],
                                supplier["lat"]
                            ]
                        }
                    }
                ]
            },
            'relationships': {
                'indicator': {
                    'data': {
                        'type': 'indicator',
                        'id': indicatorId
                    }
                }
            }
        }
    }
    return body

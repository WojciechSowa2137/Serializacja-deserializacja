from marshmallow import Schema, fields


class ProductSchema(Schema):
    id = fields.UUID(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    producer_mail = fields.Email(required=True)


json_data = {
    "id": 2, "name": "Madra ksiazka 1", "price": 3.23, "producer_mail": "fds@fds.com"
}

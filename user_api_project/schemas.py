from marshmallow import Schema, fields

class UserSchema(Schema):

    id = fields.Int(dump_only=True)

    name = fields.str(required=True)

    age = fields.Int(required=True)

    email = fields.Int(required=True)


user_schema = UserSchema()
users_schema = userSchema(many=True)
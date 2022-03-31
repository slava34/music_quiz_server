from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.String(required=True)
    username = fields.String(required=True)


class QuizesSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    level = fields.Integer(dump_only=True)
    count = fields.Integer(dump_only=True)


class AnswersSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    right = fields.Boolean(required=True)


class QuestionsSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    music_id = fields.String(required=True)
    answers = fields.Nested(AnswersSchema(many=True))


class QuizeSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    questions = fields.Nested(QuestionsSchema(many=True))


user_schema = UserSchema()
users_schema = UserSchema(many=True)

quizes_schema = QuizesSchema(many=True)


quize_schema = QuizeSchema()
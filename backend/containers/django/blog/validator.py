from graphql import GraphQLError


def validate_not_exist(query_set) -> None:
    if not query_set.exists():
        raise GraphQLError("Query result is empty")

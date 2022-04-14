# import graphene
from graphene import ObjectType,Schema,String,List,Field,Int,Mutation,ID
from graphene_django import DjangoObjectType
from authors.models import Author,Book


#level 1
# class Query(ObjectType):
#     hello = String(default_value='HI')

#level 2
# class AuthorType(DjangoObjectType):
#
#     class Meta:
#         model = Author
#         fields = '__all__'
#
#
# class Query(ObjectType):
#
#     all_author = List(AuthorType)
#
#     def resolve_all_author(root,info):
#         return Author.objects.all()

# level 3
# class AuthorType(DjangoObjectType):
#
#     class Meta:
#         model = Author
#         fields = '__all__'
#
# class BookType(DjangoObjectType):
#     class Meta:
#         model = Book
#         fields = '__all__'
#
#
#
# class Query(ObjectType):
#
#     all_author = List(AuthorType)
#
#     all_book = List(BookType)
#
#     def resolve_all_author(root,info):
#         return Author.objects.all()
#
#     def resolve_all_book(root,info):
#         return Book.objects.all()

#level 4
# class AuthorType(DjangoObjectType):
#
#     class Meta:
#         model = Author
#         fields = '__all__'
#
# class BookType(DjangoObjectType):
#     class Meta:
#         model = Book
#         fields = '__all__'
#
#
#
# class Query(ObjectType):
#
#     author_by_id = Field(AuthorType,id=Int(required=True))
#
#     def resolve_author_by_id(root,info,id=None):
#         try:
#             return Author.objects.get(id=id)
#         except Author.DoesNotExist:
#             return None
#
#     books_by_author  = List(BookType,first_name=String(required=False))
#
#     def resolve_books_by_author(root,info,first_name=None):
#         books = Book.objects.all()
#         if first_name:
#             books = books.filter(authors__first_name=first_name)
#         return books

#level 5
class AuthorType(DjangoObjectType):

    class Meta:
        model = Author
        fields = '__all__'

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'



class Query(ObjectType):

    author_by_id = Field(AuthorType,id=Int(required=True))

    def resolve_author_by_id(self,root,info,id=None):
        try:
            return Author.objects.get(id=id)
        except Author.DoesNotExist:
            return None

    books_by_author  = List(BookType,first_name=String(required=False))

    def resolve_books_by_author(root,info,first_name=None):
        books = Book.objects.all()
        if first_name:
            books = books.filter(authors__first_name=first_name)
        return books

class AuthorUpdateMutation(Mutation):

    class Arguments:
        birthday_year = Int(required=True)
        id = ID()

    author = Field(AuthorType)

    @classmethod
    def mutate(cls,root,info,birthday_year,id):
        author = Author.objects.get(id=id)
        author.birthday_year = birthday_year
        author.save()
        return AuthorUpdateMutation(author=author)


class AuthorCreateMutation(Mutation):

    class Arguments:
        birthday_year = Int(required=True)
        first_name = String()
        last_name = String()

    author = Field(AuthorType)

    @classmethod
    def mutate(cls,root,info,birthday_year,first_name,last_name):
        author = Author.objects.create(first_name=first_name,last_name=last_name,birthday_year=birthday_year)
        return AuthorUpdateMutation(author=author)


class AuthorDeleteMutation(Mutation):

    class Arguments:
        id = ID()

    author = List(AuthorType)

    @classmethod
    def mutate(cls,root,info,id):
        Author.objects.get(id=id).delete()
        return AuthorUpdateMutation(author=Author.objects.all())


class Mutations(ObjectType):
    update_author  = AuthorUpdateMutation.Field()
    create_author = AuthorCreateMutation.Field()
    delete_author = AuthorDeleteMutation.Field()



schema = Schema(query=Query,mutation=Mutations)
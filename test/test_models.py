from engine import base_engine as engine

from .settings import DEFAULT_PRICE


from api.models import Product


class ModelFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = Session()


class FactoryProduct(ModelFactory):
    sku = factory.sequence(lambda n: f"ABC{n + 1}")
    brand = factory.Faker("name")
    name = factory.Faker("name")
    description = factory.Faker("sentence")
    price = factory.sequence(lambda n: (n + 1) * DEFAULT_PRICE)
    non_discountable = factory.Faker("boolean")

    class Meta:
        model = Product


def test_product():
    product = FactoryProduct(id=2)
    assert product.price is not None


def create_factory():
    with Session(engine) as session:
        for idx in range(5):
            product_id = idx + 1
            product = FactoryProduct(id=product_id)
            data = Product(
                sku=product.sku,
                brand=product.brand,
                name=product.name,
                description=product.description,
                price=product.price,
                non_discountable=product.non_discountable,
            )
            session.add(data)
        session.commit()

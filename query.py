"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded==1903, Brand.discontinued.is_(None)).all()
# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter(Brand.founded<1950, Brand.discontinued.isnot(None)).all()
# Get any model whose brand_name is not Chevrolet.
# I got a unicode encode error when trying to print out the result in console because there is a

Model.query.filter(Model.brand_name!='Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
    result = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand).filter(Model.year==year).all()
    print "model_name\tbrand_name\theadquarters"
    for name, brand, headquarter in result:
        print name,'\t',brand,'\t', headquarter



def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    result = db.session.query(Brand.name, Model.name).join(Model).filter(Brand.name==Model.brand_name).all()
    print "brand_name\tmodel_name"
    for brand, model in result:
        print brand,'\t',model


# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    result = Brand.query.filter(db.or_(Brand.name.like('%'+mystr+'%'), Brand.name==mystr)).all()
    return result


def get_models_between(start_year, end_year):
    result = Model.query.filter(Model.year>start_year, Model.year<end_year).all()
    return result

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# The returned value is <flask_sqlalchemy.BaseQuery object at 0x104c1bc10>, and its data type is a
#class object
# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
#An association table is the table that glues two other tables that have many-to-many relationship with each other.
#Since we cannot model many-to-many relationship directly, we need a table, which is the association table,
# in the middle to serve as a bridge that connects to the two tables that we are interested in modeling using
#foreign key.
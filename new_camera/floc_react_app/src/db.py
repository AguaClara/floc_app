from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, declarative_base


# Define the base class
Base = declarative_base()

class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    base64_data = Column(String, unique=True)
    flocs = relationship('Floc', backref='image')

class Floc(Base):
    __tablename__ = 'flocs'
    id = Column(Integer, primary_key=True)
    image_id = Column(Integer, ForeignKey('images.id'))
    size = Column(Float)

# Create an engine that stores data in the local directory's

def start():
    engine = create_engine('sqlite:///floc.db')
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    return session

class DatabaseOperations:
    """
    Usage:
    db_ops = DatabaseOperations()

    # Add an image
    image = db_ops.add_image('Image 32339.jpg')

    # Add a floc to the image we just added
    db_ops.add_floc(image.id, 150.5)
    db_ops.add_floc(image.id, 200.5)
    db_ops.add_floc(image.id, 250.5)

    # Retrieve all flocs for a given image name
    flocs = db_ops.get_flocs_by_image_name('Image 32339.jpg')
    for floc in flocs:
        print(f"Floc ID: {floc.id}, Image ID: {floc.image_id}, Size: {floc.size}")

    # Close the connection when done
    db_ops.close()
    """
    def __init__(self, session):
        self.session = session

    
    def add_image(self, image_name, image_base64):
        existing_image = self.session.query(Image).filter_by(base64_data=image_base64).first()
        if existing_image:
            return existing_image
        new_image = Image(name=image_name, base64_data=image_base64)
        self.session.add(new_image)
        self.session.commit()
        return new_image

    def add_floc(self, image_id, size):
        new_floc = Floc(image_id=image_id, size=size)
        self.session.add(new_floc)
        self.session.commit()
        return new_floc
    
    def get_current_image_id(self):
        result = self.session.query(Image.id).order_by(Image.id.desc()).first()
        if result:
            return result[0]
        return -1
    
    def get_image_base64_data(self, id):
        image = self.session.query(Image).filter_by(id=id).first()
        if image:
            return image.base64_data
        return ""

    def get_flocs_by_image_name(self, image_name):
        return self.session.query(Floc).join(Image).filter(Image.name == image_name).all()

    def close(self):
        self.session.close()
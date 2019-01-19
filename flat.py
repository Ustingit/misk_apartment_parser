class Flat:

    name = None
    author = None
    price = None
    phone = None
    description = None
    phoneImgBinary = None
    mainApPhotoBinary = None
    creationDate = None
    actualToDate = None
    isActive = None
    isDonated = None
    donateDueDate = None
    internalComment = None
    clientId = None
    parsingSource = None
    shortId = None
    mainPhotoUrl = None
    photosListUrls = None

    def __init__(self, name=None, author=None, price=None, phone=None, description=None, phoneImgBinary=None,
                 mainApPhotoBinary=None, creationDate=None, actualToDate=None, isActive=None,
                 isDonated=None, donateDueDate=None, internalComment=None, clientId=None, parsingSource=None,
                 shortId=None, mainPhotoUrl=None, photosListUrls=None):
        self.name = name
        self.author = author
        self.price = price
        self.phone = phone
        self.description = description
        self.phoneImgBinary = phoneImgBinary
        self.mainApPhotoBinary = mainApPhotoBinary
        self.creationDate = creationDate
        self.actualToDate = actualToDate
        self.isActive = isActive
        self.isDonated = isDonated
        self.donateDueDate = donateDueDate
        self.internalComment = internalComment
        self.clientId = clientId
        self.parsingSource = parsingSource
        self.shortId = shortId
        self.mainPhotoUrl = mainPhotoUrl
        self.photosListUrls = photosListUrls

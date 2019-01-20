class Flat:

    name = None
    author = None
    price = None
    phone = None
    description = None
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
    sourceURL = None
    phoneImgURL = None

    def __init__(self, name=None, author=None, price=None, phone=0, description=None, creationDate=None,
                 actualToDate=None, isActive=0, isDonated=0, donateDueDate=None, internalComment=None,
                 clientId=0, parsingSource=0, shortId=None, mainPhotoUrl=None, photosListUrls=None,
                 sourceURL=None, phoneImgURL=None):
        self.name = name
        self.author = author
        self.price = price
        self.phone = phone
        self.description = description
        self.creationDate = creationDate
        self.actualToDate = actualToDate
        self.isActive = isActive
        self.isDonated = isDonated
        self.donateDueDate = donateDueDate
        self.internalComment = internalComment
        self.clientId = clientId
        self.parsingSource = parsingSource
        self.sourceURL = sourceURL
        self.shortId = shortId
        self.mainPhotoUrl = mainPhotoUrl
        self.photosListUrls = photosListUrls
        self.phoneImgURL = phoneImgURL

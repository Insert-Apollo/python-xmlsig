from cryptography.hazmat import primitives
from cryptography.x509 import oid

# Namespaces
DSigNs = 'http://www.w3.org/2000/09/xmldsig#'
EncNs = 'http://www.w3.org/2001/04/xmlenc#'
XPathNs = 'http://www.w3.org/TR/1999/REC-xpath-19991116'
XPath2Ns = 'http://www.w3.org/2002/06/xmldsig-filter2'
XPointerNs = 'http://www.w3.org/2001/04/xmldsig-more/xptr'
Soap11Ns = 'http://schemas.xmlsoap.org/soap/envelope/'
Soap12Ns = 'http://www.w3.org/2002/06/soap-envelope'
NsExcC14N = 'http://www.w3.org/2001/10/xml-exc-c14n#'
NsExcC14NWithComments = 'http://www.w3.org/2001/10/xml-exc-c14n#WithComments'

NS_MAP = {'ds': DSigNs}

TransformInclC14N = 'http://www.w3.org/TR/2001/REC-xml-c14n-20010315'
TransformInclC14NWithComments = 'http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments'
TransformInclC14N11 = ''
TransformInclC14N11WithComments = ''
TransformExclC14N = 'http://www.w3.org/2001/10/xml-exc-c14n#'
TransformExclC14NWithComments = 'http://www.w3.org/2001/10/xml-exc-c14n#WithComments'
TransformEnveloped = u'http://www.w3.org/2000/09/xmldsig#enveloped-signature'
TransformXPath = 'http://www.w3.org/TR/1999/REC-xpath-19991116'
TransformXPath2 = ''
TransformXPointer = ''
TransformXslt = 'http://www.w3.org/TR/1999/REC-xslt-19991116'
TransformRemoveXmlTagsC14N = ''
TransformVisa3DHack = ''
TransformAes128Cbc = ''
TransformAes192Cbc = ''
TransformAes256Cbc = ''
TransformKWAes128 = ''
TransformKWAes192 = ''
TransformKWAes256 = ''
TransformDes3Cbc = ''
TransformKWDes3 = ''
TransformDsaSha1 = 'http://www.w3.org/2000/09/xmldsig#dsa-sha1'
TransformDsaSha256 = 'http://www.w3.org/2000/09/xmldsig#dsa-sha256'
TransformEcdsaSha1 = 'http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha1'
TransformEcdsaSha224 = 'http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha224'
TransformEcdsaSha256 = 'http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256'
TransformEcdsaSha384 = 'http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha384'
TransformEcdsaSha512 = 'http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha512'
TransformHmacMd5 = ''
TransformHmacRipemd160 = ''
TransformHmacSha1 = ''
TransformHmacSha224 = ''
TransformHmacSha256 = ''
TransformHmacSha384 = ''
TransformHmacSha512 = ''
TransformRsaMd5 = 'http://www.w3.org/2001/04/xmldsig-more#rsa-md5'
TransformRsaRipemd160 = 'http://www.w3.org/2001/04/xmldsig-more#rsa-ripemd160'
TransformRsaSha1 = 'http://www.w3.org/2000/09/xmldsig#rsa-sha1'
TransformRsaSha224 = 'http://www.w3.org/2001/04/xmldsig-more#rsa-sha224'
TransformRsaSha256 = 'http://www.w3.org/2001/04/xmldsig-more#rsa-sha256'
TransformRsaSha384 = 'http://www.w3.org/2001/04/xmldsig-more#rsa-sha384'
TransformRsaSha512 = 'http://www.w3.org/2001/04/xmldsig-more#rsa-sha512'
TransformRsaPkcs1 = ''
TransformRsaOaep = ''
TransformMd5 = 'http://www.w3.org/2001/04/xmldsig-more#md5'
TransformRipemd160 = 'http://www.w3.org/2001/04/xmlenc#ripemd160'
TransformSha1 = 'http://www.w3.org/2000/09/xmldsig#sha1'
TransformSha224 = 'http://www.w3.org/2001/04/xmldsig-more#sha224'
TransformSha256 = 'http://www.w3.org/2001/04/xmlenc#sha256'
TransformSha384 = 'http://www.w3.org/2001/04/xmldsig-more#sha384'
TransformSha512 = 'http://www.w3.org/2001/04/xmlenc#sha512'

TransformUsageUnknown = ''
TransformUsageDSigTransform = [
    TransformEnveloped
]
TransformUsageC14NMethod = {
    TransformInclC14N: {
        'method': 'c14n',
        'exclusive': False,
        'comments': False
    },
    TransformInclC14NWithComments: {
        'method': 'c14n',
        'exclusive': False,
        'comments': True
    },
    TransformExclC14N: {
        'method': 'c14n',
        'exclusive': True,
        'comments': False
    },
    TransformExclC14NWithComments: {
        'method': 'c14n',
        'exclusive': True,
        'comments': False
    }
}

TransformUsageDSigTransform.extend(TransformUsageC14NMethod.keys())

TransformUsageDigestMethod = {
    TransformMd5: 'md5',
    TransformSha1: 'sha1',
    TransformSha224: 'sha224',
    TransformSha256: 'sha256',
    TransformSha384: 'sha384',
    TransformSha512: 'sha512',
    TransformRipemd160: 'ripemd160',
}
TransformUsageSignatureMethod = {
    TransformRsaMd5: {
        'digest': primitives.hashes.MD5,
        'private_key_class': primitives.asymmetric.rsa.RSAPrivateKey,
        'public_key_class': primitives.asymmetric.rsa.RSAPublicKey
    },
    TransformRsaSha1: {
        'digest': primitives.hashes.SHA1,
        'private_key_class': primitives.asymmetric.rsa.RSAPrivateKey,
        'public_key_class': primitives.asymmetric.rsa.RSAPublicKey
    },
    TransformRsaSha224: {
        'digest': primitives.hashes.SHA224,
        'private_key_class': primitives.asymmetric.rsa.RSAPrivateKey,
        'public_key_class': primitives.asymmetric.rsa.RSAPublicKey
    },
    TransformRsaSha256: {
        'digest': primitives.hashes.SHA256,
        'private_key_class': primitives.asymmetric.rsa.RSAPrivateKey,
        'public_key_class': primitives.asymmetric.rsa.RSAPublicKey
    },
    TransformRsaSha384: {
        'digest': primitives.hashes.SHA384,
        'private_key_class': primitives.asymmetric.rsa.RSAPrivateKey,
        'public_key_class': primitives.asymmetric.rsa.RSAPublicKey
    },
    TransformRsaSha512: {
        'digest': primitives.hashes.SHA512,
        'private_key_class': primitives.asymmetric.rsa.RSAPrivateKey,
        'public_key_class': primitives.asymmetric.rsa.RSAPublicKey
    },
    TransformDsaSha1: {
        'digest': primitives.hashes.SHA1,
        'private_key_class': primitives.asymmetric.dsa.DSAPrivateKey,
        'public_key_class': primitives.asymmetric.dsa.DSAPublicKey
    },
    TransformDsaSha256: {
        'digest': primitives.hashes.SHA256,
        'private_key_class': primitives.asymmetric.dsa.DSAPrivateKey,
        'public_key_class': primitives.asymmetric.dsa.DSAPublicKey
    },
}
TransformUsageEncryptionMethod = {}
TransformUsageAny = {}
OID_NAMES = {
    oid.NameOID.COMMON_NAME: 'CN',
    oid.NameOID.COUNTRY_NAME: 'C',
    oid.NameOID.DOMAIN_COMPONENT: 'DC',
    oid.NameOID.EMAIL_ADDRESS: 'E',
    oid.NameOID.GIVEN_NAME: 'G',
    oid.NameOID.LOCALITY_NAME: 'L',
    oid.NameOID.ORGANIZATION_NAME: 'O',
    oid.NameOID.ORGANIZATIONAL_UNIT_NAME: 'OU',
    oid.NameOID.SURNAME: 'SN'
}
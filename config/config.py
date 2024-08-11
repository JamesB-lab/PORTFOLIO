from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
import os

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class DjangoConfig:
    secret_key: str
    debug: bool

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AccessKeyConfig:
    id: str
    secret: str

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SESConfig:
    region: str

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SignerConfig:
    id: str
    private_key: str

    def __init__(self, id: str, private_key: str):
        self.id = id.strip()
        self.private_key = private_key.encode('ascii').strip()

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CloudfrontConfig:
    signer: SignerConfig
    custom_domain: str

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class S3Config:
    bucket_name: str
    region_name: str
    signature_version: str
    expiration: int
    static_location: str

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AWSConfig:
    access_key: AccessKeyConfig
    ses: SESConfig
    s3: S3Config
    cloudfront: CloudfrontConfig

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Config:
    django: DjangoConfig
    aws: AWSConfig

def load_config() -> Config:
    if os.path.exists('config.json'):
        with open('config.json', 'r') as f:
            c = f.read()
    else:
        c = os.environ.get('CONFIG')
    if c is None:
        raise Exception('neither the file config.json nor the env var CONFIG exist')
    return Config.schema().loads(c)


config = load_config()

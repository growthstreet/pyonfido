class DocumentType():
    Passport = "passport"
    NationalIdentityCard = "national_identity_card"
    WorkPermit = "work_permit"
    DrivingLicense = "driving_license"
    NationalInsurance = "national_insurance"
    BirthCertificate = "birth_certificate"
    BankStatement = "bank_statement"
    Unknown = "unknown"

default_page = 1

default_per_page = 20


class ApiResource(object):
    def __init__(self, requestor):
        self.requestor = requestor

    def post(self, url, data):
        return self.requestor.post(url, data)

    def get(self, url, data=None):
        return self.requestor.get(url, data)


class Applicants(ApiResource):
    def create(self, applicant_details):
        return self.post("applicants", applicant_details)

    def find(self, applicant_id):
        return self.get("applicants/{0}".format(applicant_id))

    def all(self, page=default_page, per_page=default_per_page):
        params = {
            "page": page,
            "per_page": per_page
        }

        return self.get("applicants", params)


class Documents(ApiResource):
    def create(self, applicant_id, document_details):
        return self.post("applicants/{0}/documents/".format(applicant_id),
                         document_details)


class Checks(ApiResource):
    def create(self, applicant_id, check_details):
        return self.post("applicants/{0}/checks".format(applicant_id),
                         check_details)

    def find(self, applicant_id, check_id):
        return self.get("applicants/{0}/checks/{1}".format(applicant_id,
                        check_id))

    def all(self, applicant_id, page=default_page, per_page=default_per_page):
        params = {
            "page": page,
            "per_page": per_page
        }

        return self.get("applicants/{0}/checks".format(applicant_id), params)


class Reports(ApiResource):
    def find(self, check_id, report_id):
        return self.get("checks/{0}/reports/{1}".format(check_id, report_id))

    def all(self, check_id):
        return self.get("checks/{0}/reports".format(check_id))


class AddressPicker(ApiResource):
    def all(self, postcode):
        params = {
            "postcode": postcode
        }

        return self.get("applicants/addresses/pick", params)
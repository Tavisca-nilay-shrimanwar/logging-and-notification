import boto3

#############################################################################
############################# EMAIL UTIL ####################################
#############################################################################

################## Requirements ######################################
# Need to have a identity created in SES first before sending the email. 
# Identity can be either domain or email address
# AWS will send a confirmation email to the mail address
# We need to verify by clicking the link in the email.
# And then we can send the email using boto3.

class Email():
    CHARSET = "UTF-8"
     
    def __init__(self, **kwargs) -> None:
        self.client = boto3.client("ses")
        self.sender = kwargs["sender"]
        self.receiver = kwargs["receiver"]

    def send_success_email(self, **opts):
        content = self.get_success_template(opts["content"])
          
        return self.client.send_email(
            Destination={
                "ToAddresses": [
                    self.receiver
                ],
            },
            Message={
                "Body": {
                        "Html": {
                            "Charset": self.CHARSET,
                            "Data": content,
                        }
                },
                "Subject": {
                        "Charset": self.CHARSET,
                        "Data": opts["subject"],
                },
            },
            Source=self.sender
        )

    def send_failure_email(self, **opts):
        content = self.get_failure_template(opts["content"])
        
        return self.client.send_email(
            Destination={
                "ToAddresses": [
                    self.receiver
                ],
            },
            Message={
                "Body": {
                        "Html": {
                            "Charset": self.CHARSET,
                            "Data": content,
                        }
                },
                "Subject": {
                        "Charset": self.CHARSET,
                        "Data": opts["subject"],
                },
            },
            Source=self.sender
        )

    def get_success_template(self, content: str):
        return """
            <html>
                <head></head>
                <h3 style='color:green'>Success</h3>
                <p>{content}</p>
                </body>
            </html>
        """.format(content=content)

    def get_failure_template(self, content: str):
        return """
            <html>
                <head></head>
                <h3 style='color:red'>Failure</h3>
                <p>{content}</p>
                </body>
            </html>
        """.format(content=content)

################## Usage Example ######################################
# email = Email(
#     sender="ganesh.lohar@tavisca.com",
#     receiver="nilay.shrimanwar@tavisca.com"
# )
# email.send_success_email(
#     subject="Backup success",
#     content="This is a success email details"
# )
# email.send_failure_email(
#     subject="Backup failed",
#     content="This is a failure email details"
# )
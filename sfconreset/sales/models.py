from salesforce import models as models

class Account(models.Model):
    is_deleted = models.BooleanField(
        verbose_name='Deleted', sf_read_only=models.READ_ONLY)
    name = models.CharField(max_length=255, verbose_name='Account Name')
    type = models.CharField(max_length=40, verbose_name='Account Type', choices=[('Analyst', 'Analyst'), ('Competitor', 'Competitor'), ('Customer', 'Customer'), ('Integrator', 'Integrator'), (
        'Investor', 'Investor'), ('Partner', 'Partner'), ('Press', 'Press'), ('Prospect', 'Prospect'), ('Reseller', 'Reseller'), ('Other', 'Other')], blank=True, null=True)
    allowed_features = models.CharField(custom=True, db_column='Allowed_Features__c',
                                        max_length=4099, verbose_name='Allowed Features', blank=True, null=True)
    use_customer_account = models.BooleanField(
        custom=True, db_column='Use_Customer_Account__c', verbose_name="Use Customer's Account", default=models.DEFAULTED_ON_CREATE)
    vat_registration_status = models.CharField(custom=True, db_column='VAT_Registration_Status__c', max_length=255, verbose_name='VAT Registration Status', choices=[
        ('Registered', 'Registered'), ('Not VAT-Registered', 'Not VAT-Registered')], blank=True, null=True)
    vat = models.CharField(custom=True, db_column='VAT__c',
                           max_length=255, verbose_name='VAT #', blank=True, null=True)
    tax_vat_document_url = models.URLField(custom=True, db_column='TAX_VAT_Document_URL__c',
                                           max_length=255, verbose_name='TAX/VAT Document URL', blank=True, null=True)
    tax_exempt_certificate = models.CharField(custom=True, db_column='Tax_Exempt_Certificate__c',
                                              max_length=255, verbose_name='Tax Exempt Certificate #', blank=True, null=True)
    taxable = models.CharField(custom=True, max_length=255, default=models.DEFAULTED_ON_CREATE, choices=[
        ('Taxable', 'Taxable'), ('Non-Taxable', 'Non-Taxable')], blank=True, null=True)
    preferred_carrier = models.CharField(custom=True, db_column='Preferred_Carrier__c', max_length=255, verbose_name='Preferred Carrier', default=models.DEFAULTED_ON_CREATE, choices=[
        ('FEDEX', 'FedEx'), ('UPS', 'UPS'), ('BIOCARE', 'BioCare'), ('OTHER', 'Other'), ('MANUAL', 'Manual')], blank=True, null=True)
    customer_account_number = models.CharField(custom=True, db_column='Customer_Account_Number__c',
                                               max_length=255, verbose_name="Customer's Account Number", blank=True, null=True)
    ein_number = models.CharField(custom=True, db_column='EIN_Number__c', max_length=50, verbose_name='EIN Number', blank=True, null=True)

    class Meta(models.Model.Meta):
        db_table = 'Account'
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'


class Contact(models.Model):
    is_deleted = models.BooleanField(
        verbose_name='Deleted', sf_read_only=models.READ_ONLY)
    master_record = models.ForeignKey(
        'self', models.DO_NOTHING, related_name='contact_masterrecord_set', sf_read_only=models.READ_ONLY, blank=True, null=True)
    account = models.ForeignKey(Account, models.DO_NOTHING, blank=True, null=True,
                                related_name='contacts', related_query_name='contact')  # Master Detail Relationship *
    last_name = models.CharField(max_length=80)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    salutation = models.CharField(max_length=40, choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms.'), (
        'Mrs.', 'Mrs.'), ('Dr.', 'Dr.'), ('Prof.', 'Prof.')], blank=True, null=True)
    name = models.CharField(
        max_length=121, verbose_name='Full Name', sf_read_only=models.READ_ONLY)
    email = models.EmailField(blank=True, null=True)
    used_by_e_commerce = models.BooleanField(
        default=True, custom=True, db_column='Used_by_eCommerce__c', max_length=255, verbose_name='Used by eCommerce')


class CustomVector(models.Model):
    name = models.CharField(max_length=80, verbose_name='Custom Vector Name',
                            default=models.DEFAULTED_ON_CREATE, blank=True, null=True)
    date_approved = models.DateField(
        custom=True, db_column='Date_approved__c', verbose_name='Date approved', blank=True, null=True)
    mes_uid = models.CharField(custom=True, db_column='MES_UID__c',
                               max_length=255, verbose_name='MES UID', blank=True, null=True)
    type = models.CharField(custom=True, max_length=255, choices=[(
        'Custom', 'Custom'), ('Catalog', 'Catalog')], blank=True, null=True)

    class Meta(models.Model.Meta):
        db_table = 'CustomVector__c'
        verbose_name = 'Custom Vector'
        verbose_name_plural = 'Customs Vectors'


class CustomVectorForContact(models.Model):
    is_deleted = models.BooleanField(
        verbose_name='Deleted', sf_read_only=models.READ_ONLY)
    name = models.CharField(
        max_length=80, verbose_name='Custom Vector for contacts Name', sf_read_only=models.READ_ONLY)
    contact = models.ForeignKey(Contact, models.DO_NOTHING, related_name="vectors_for_contact",
                                custom=True, sf_read_only=models.NOT_UPDATEABLE)  # Master Detail Relationship 0
    vector = models.ForeignKey(CustomVector, models.DO_NOTHING,
                               related_name="contacts_for_vector", db_column='CustomVector__c', custom=True)

    class Meta(models.Model.Meta):
        db_table = 'CustomVectorforcontacts__c'
        verbose_name = 'Custom Vector for contacts'
        verbose_name_plural = 'Custom Vectors for contacts'
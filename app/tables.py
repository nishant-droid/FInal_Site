from flask_table import Table, Col

class Master_Bank_Table(Table):
    Sr_No = Col("Serial Number")
    Bank_Code = Col("Bank Code")
    Bank_Name = Col("Bank Name")
    Bank_Acc_Details = Col("Bank Account Details")
    Address = Col("Address")
    Miscelleneous = Col("Misscelleneous/ Remark")

class Data(object):
    def __init__(self,Sr_No,bankcode,bankname,bankaccdetails, address, miscelleneous,branchcode,branchname,atmcode,email,eamilgroup,bankadd,mftid,sitename,district,cassetteconfig,cashlivedate,techlivedate,ubscode,routenumber,sequencenumber,atmserialnumber,secretaryname,secretarynumber,enginnername,engineernumber,cashremovaldate,cashremovalreason,closuretype,closuredate,closureremark,salarypaymentdate,salaryperpayment):
        mftid,sitename,ditrict,cassetteconfig,cashlivedate,techlivedate,ubscode,routenumber,sequencenumber,atmserialnumber,secretaryname,secretarynumber,enginnername,engineernumber,cashremovaldate,cashremovalreason,closuretype,closureremark,salarypaymentdate,salaryperpayment
        self.Sr_No = Sr_No
        self.Bank_Code = bankcode
        self.Bank_Name = bankname    
        self.Bank_Acc_Details = bankaccdetails
        self.Address = address
        self.Miscelleneous = miscelleneous
        self.Branch_Code = branchcode
        self.Branch_Name = branchname
        self.ATM_Code = atmcode
        self.Bank_Code = bankcode
        self.Email = email
        self.Email_Group = eamilgroup
        self.MFT_ID = mftid
        self.Site_Name = sitename
        self.District = district
        self.Cassette_Config = cassetteconfig
        self.Cash_Live_Date = cashlivedate
        self.Tech_Live_Date = techlivedate
        self.UBS_Code = ubscode
        self.Route_Number = routenumber
        self.Sequence_Number = sequencenumber
        self.ATM_Serial_Number = atmserialnumber
        self.Secretary_Name = secretaryname
        self.Secretary_Number = secretarynumber
        self.Engineer_Name = enginnername
        self.Engineer_Number = engineernumber
        self.Cash_Removal_Date = cashremovaldate
        self.Cash_Removal_Reason = cashremovalreason
        self.Closure_Type = closuretype
        self.Closure_Date = closuredate
        self.Closure_Remark = closureremark
        self.Salary_Payment_Date = salarypaymentdate
        self.Salary_Per_Payment = salaryperpayment
        
        

class Master_Branch_Table(Table):
    Sr_No = Col("Serial Number")
    Branch_Code = Col("Branch Code")
    Branch_Name = Col("Branch Name")
    ATM_Code = Col("ATM Code")
    Bank_Code = Col("Bank Code")
    Bank_Add = Col("Bank Address")
    Email = Col("Email")
    Email_Group = Col("Email Group")

class Master_CIT_Table(Table):
    Sr_No = Col("Serial Number")
    CIT_Code = Col("CIT Code")
    CIT_Name = Col("CIT Name")
    CIT_Bank_Acc_Details = Col("Bank Accout Details")
    CIT_Address = Col("Address")
    Contact_Person_Name = Col("Contact Person Name")
    Contact_Person_Number = Col("Contact Person Number")
    Contact_Person_Email = Col("Contact Person Email")

class Master_MFT_Table(Table):
    Sr_No = Col("Serial Number")
    MFT_ID = Col("MFT ID")
    Site_Name = Col("Site Name")
    District = Col("District")
    Bank_Code = Col("Bank Code")
    Branch_Code = Col("Branch Code")
    CIT_Name = Col("CIT Name")
    CIT_Code = Col("CIT Code")
    Cassette_Config = Col("Cassette Configuration")
    Cash_Live_Date = Col("Cash Live Date")
    Tech_Live_Date = Col("Tech Live Date")
    UBS_Code = Col("UBS Code")
    Route_Number = Col("Route Number")
    Sequence_Number = Col("Sequence Number")
    ATM_Serial_Number = Col("ATM Serial Number")
    Secretary_Name = Col("Secretary Name")
    Secretary_Number = Col("Secretary Number")
    Engineer_Name = Col("Enigneer Name")
    Engineer_Number = Col("Engineer Number")
    Cash_Removal_Date = Col("Cash Removal Date")
    Cash_Removal_Reason = Col("Cash Removal Reason")
    Closure_Type = Col("Closure Type")
    Closure_Date = Col("Closure Date")
    Closure_Remark = Col("Closure Remark")
    Salary_Payment_Date = Col("Salary Payment Date")
    Salary_Per_Payment = Col("Salary Per Payment")
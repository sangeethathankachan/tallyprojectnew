from django.shortcuts import render,redirect
import os
from app1.models import crtcompony,GroupModel
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'home.html')

def changecompony(request):
    return render(request, 'changecompony.html')

def createcompony(request):
    return render(request, 'createcompony.html')

def crtecompony(request):
    if request.method=='POST':
        comname=request.POST['componyname']
        mailingname=request.POST['mailingname']
        address=request.POST['address']
        state=request.POST['state']
        country=request.POST['country']
        pincode=request.POST['pincode']
        telphone=request.POST['telphone']
        mobile=request.POST['mobile']
        fax=request.POST['fax']
        email=request.POST['email']
        website=request.POST['website']
        fyearbgn=request.POST['fyearbgn']
        booksbgn=request.POST['booksbgn']
        curncysymbl=request.POST['curncysymbl']
        crncyname=request.POST['crncyname']
        # items=request.FILES['file']
        data=crtcompony(componyname=comname,
                    mailingname=mailingname,
                    address=address,
                    state=state,
                    country=country,
                    pincode=pincode,
                    telphone=telphone,
                    mobile=mobile,
                    fax=fax,
                    email=email,
                    website=website,
                    fyearbgn=fyearbgn,
                    booksbgn=booksbgn,
                    curncysymbl=curncysymbl,
                    crncyname=crncyname)
        data.save()
        messages.success(request,"Group added successfully!")
        
        return redirect('/')


def changecompony(request):
    data=crtcompony.objects.all()
    return render(request,'changecompony.html',{'data':data})

def selectcompony(request):
    data=crtcompony.objects.all()
    return render(request,'selectcompony.html',{'data':data})
    

def group(request):
        return render(request, 'group.html')

def editgroup(request):
    return render(request,'editgroup.html')

        
@csrf_exempt
def create_group(request):
    if request.method == 'POST':
        gname = request.POST['gname']
        alia = request.POST['alia']
        under = request.POST['und']
        gp = request.POST['subled']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']

        mdl = GroupModel(
            name=gname,
            alias=alia,
            under=under,
            gp_behaves_like_sub_ledger=gp,
            nett_debit_credit_bal_reporting=nett,
            used_for_calculation=calc,
            method_to_allocate_usd_purchase=meth,
        )
        mdl.save()
        # return redirect('index_view')
        messages.success(request,"Compony added successfully!")
        
        return redirect('/')

def groups(request):
    mdl=GroupModel.objects.all()
    return render(request,'groups.html',{'mdl':mdl})

def ledger(request):
    return render(request,'ledger.html')

def create_ledger(request):
    if request.method == 'POST':

        # Ledger Basic
        Lname = request.POST['Lname']
        Lalias = request.POST['Lalias']
        Lunder = request.POST['Lund']
        try:
            mdl = GroupModel.objects.get(name=Lunder)

            fl = mdl
            print('IN name')
        except:

            try:
                mdl = GroupModel.objects.get(alias=Lunder)
                print('in ALIAS')
                fl = mdl
            except:
                print("NOT found")

        Lopening_bal = request.POST['Lopening']
        typ_of_ledg = request.POST['typ_of_ledg']
        typ_of_duty = request.POST['typ_of_duty']
        percet_of_calc = request.POST['percet_of_calc']
        main_balance_bill_ = request.POST['main_balance_bill_']  # bool
        chk_credit_days = request.POST['chk_credit_days']  # bool
        def_cr_period = request.POST['def_cr_period']
        # Provide Banking Details
        provide_banking = request.POST['provide_banking']  # bool

        # Banking_details
        B_od_limit = request.POST['B_od_limit']
        B_ac_holder_name = request.POST['B_ac_name']
        B_ac_no = request.POST['B_ac_no']
        B_ifsc = request.POST['B_ac_ifsc']
        B_swift_code = request.POST['B_ac_swift']
        B_name = request.POST['B_name']
        B_branch = request.POST['B_branch']
        '''bank Configuration'''
        B_alter_chq_bks = request.POST['B_alter_chq_bks']  # bool
        B_name_enbl_chq_prtg = request.POST['B_name_enbl_chq_prtg']  # bool

        # Mailing_details
        Mname = request.POST['Mname']
        Maddress = request.POST['Maddress']
        Mstate = request.POST['Mstate']
        Mcountry = request.POST['Mcountry']
        Mpincode = request.POST['Mpincode']

        # Tax_Registration_Details
        Tgst_uin = request.POST['Tgst_uin']
        Treg_typ = request.POST['Treg_typ']
        Tpan_no = request.POST['Tpan_no']
        T_alter_gst = request.POST['T_alter_gst']

        # Satutory Details
        assemble_calc = request.POST['assemble_value']
        is_gst_applicable = request.POST['is_gst_applicable']
        typ_of_supply = request.POST['typ_of_supply']

        # -------------------------#
        sec = CompanyModel.objects.get(id=request.session["scid"])
        Lmdl = LedgerModel(
            cid=sec,
            ledger_name=Lname,
            ledger_alias=Lalias,
            group=fl,
            ledger_opening_bal=Lopening_bal,
            ledger_type=typ_of_ledg,
            type_of_duty=typ_of_duty,
            percent_of_calculation=percet_of_calc,
            maintain_bal_bill=main_balance_bill_,
            credit_days_during_voucher_entry=chk_credit_days,
            default_cr_peroid=def_cr_period,
            provide_banking_details=provide_banking,
        )
        Lmdl.save()
        idd = Lmdl
        Bmdl = BankingDetails(
            cid=sec,
            ledger_id=idd,
            od_limit=B_od_limit,
            holder_name=B_ac_holder_name,
            ac_number=B_ac_no,
            ifsc=B_ifsc,
            swift_code=B_swift_code,
            bank_name=B_name,
            branch_name=B_branch,
            alter_chk_bks=B_alter_chq_bks,
            enbl_chk_printing=B_name_enbl_chq_prtg,
        )
        Bmdl.save()
        M_mdl = MailingAddressModel(
            cid=sec,
            ledger_id=idd,
            name=Mname,
            address=Maddress,
            state=Mstate,
            country=Mcountry,
            pincode=Mpincode,
        )
        M_mdl.save()
        T_mdl = TaxRegisterModel(
            cid=sec,
            ledger_id=idd,
            gst_uin=Tgst_uin,
            register_type=Treg_typ,
            pan_no=Tpan_no,
            alter_gst_details=T_alter_gst,

        )
        T_mdl.save()
        LS_mdl = LedgerSatutoryModel(
            cid=sec,
            ledger_id=idd,
            assessable_calculation=assemble_calc,
            gst_applicable=is_gst_applicable,
            type_of_supply=typ_of_supply,


        )
        LS_mdl.save()
        return redirect('index_view')

    grp_under_lst = GroupModel.objects.all().order_by('name')
  
    context = {
        'grp': grp_under_lst,
        
    }
    return render(request, 'create_ledger.html', context)
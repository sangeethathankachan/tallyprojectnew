from django.shortcuts import render,redirect
import os
from app1.models import CurrencyAlter,CreateCurrency,crtcompony,GroupModel,create_stockgrp,create_stockcate,create_stockitem,units,create_goddown
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def base(request):
    return render(request, 'base.html')

def godown(request):
    return render(request, 'godown.html')

def stockgroup(request):
    return render(request, 'stockgroup.html')

def stockcategory(request):
    return render(request, 'stockcategory.html')

def update_voucher(request):
    return render(request, 'update_voucher.html')

def stockitem(request):
    return render(request, 'stockitem.html')

def unit(request):
    return render(request, 'unit.html')

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

def currency(request):
    return render(request,'currency.html')

def currencycreate(request):
    return render(request,'currencycreate.html')


def create_currency(request):
    if request.method == 'POST':
        symbol = request.POST['symbol']
        fname = request.POST['fname']
        if len(symbol) <= 0:
            print('XX')
            return JsonResponse({
                'status': 00
            })
        elif len(fname) <= 0:
            print('XXX')
            return JsonResponse({
                'status': 00
            })
        else:
            pass

        iso_code = request.POST['iso_code']
        n_deci_placs = request.POST['n_deci_placs']
        smt_millon = request.POST['smt_millon']
        symbol_to_amount = request.POST['symbol_to_amount']
        space_bt_sy = request.POST['space_bt_sy']
        amount_after_decimal = request.POST['amount_after_decimal']
        amount_in_words = request.POST['amount_in_words']

        mdl_obj = CreateCurrency(
            symbol=symbol,
            formal_name=fname,
            ISO_code=iso_code,
            decimal_places=n_deci_placs,
            show_in_millions=smt_millon,
            suffix_to_amount=symbol_to_amount,
            space_symbol_amount=space_bt_sy,
            word_after_decimal=amount_after_decimal,
            decimal_no_in_words=amount_in_words,
        )
        mdl_obj.save()
        return redirect('load_create_currency')


def voucher(request):
    return render(request,'voucher.html')

def createvoucher(request):
    return render(request,'createvoucher.html')

def save_ledger(request):
    if request.method == 'POST':
        # Ledger Basic
        Lname = request.POST.get('ledger_name', False)
        Lalias = request.POST.get('ledger_alias', False)
        Lunder = request.POST.get('group_under', False)
        Lopening_bal = request.POST.get('ledger_opening_bal', False)
        typ_of_ledg = request.POST.get('ledger_type', False)
        provide_banking = request.POST.get('provide_banking_details', False)

        # Banking_details
        B_od_limit = request.POST.get('od_limit', False)
        B_ac_holder_name =request.POST.get('holder_name', False)
        B_ac_no = request.POST.get('ac_number', False)
        B_ifsc = request.POST.get('ifsc', False)
        B_swift_code =request.POST.get('swift_code', False)
        B_name = request.POST.get('bank_name', False)
        B_branch = request.POST.get('branch_name', False)
        B_alter_chq_bks =request.POST.get('alter_chk_bks', False)
        B_name_enbl_chq_prtg = request.POST.get('enbl_chk_printing', False) 
        B_chqconfg= request.POST.get('chqconfg', False) 
        # Mailing_details
        Mname = request.POST.get('name', False)
        Maddress = request.POST.get('address', False)
        Mstate =request.POST.get('state', False)
        Mcountry = request.POST.get('country', False)
        Mpincode = request.POST.get('pincode', False)

        # Tax_Registration_Details
        Tgst_uin = request.POST.get('gst_uin', False)
        Treg_typ = request.POST.get('register_type', False)
        Tpan_no = request.POST.get('pan_no', False)
        T_alter_gst =request.POST.get('alter_gst_details', False)

        # Satutory Details
        assessable_calculationn = request.POST.get('assessable_calculation', False)
        Appropriate_too =request.POST.get('Appropriate_to', False)
        gst_applicablee = request.POST.get('is_gst_applicable',False)
        Set_alter_GSTT=request.POST.get('Set_alter_GST', False)
        type_of_supplyy = request.POST.get('type_of_supply',False)
        Method_of_calcc=request.POST.get('Method_of_calc', False)

        #leadger Rounding
        ledger_idd=request.POST.get('useadvc', False)
        Rounding_Methodd=request.POST.get('Rounding_Method', False)
        Round_limitt =request.POST.get('Round_limit', False)

        #ledger_tax 
        type_of_duty_or_taxx=request.POST.get('type_of_duty_or_tax', False)
        type_of_taxx=request.POST.get('type_of_tax', False)
        valuation_typee=request.POST.get('valuation_type', False)
        rate_per_unitt=request.POST.get('rate_per_unit', False)
        Persentage_of_calculationn=request.POST.get('Persentage_of_calculation', False)

        #sundry
        maintain_balance_bill_by_billl=request.POST.get('maintain_balance_bill_by_bill', False)
        Default_credit_periodd=request.POST.get('Default_credit_period', False)
        Check_for_credit_dayss=request.POST.get('Check_for_credit_days', False)

        if Ledger.objects.filter(ledger_name = Lname ).exists():
                messages.info(request,'This Name is already taken...!')
                return redirect('load_create_ledger.html')

        Lmdl = Ledger(
            ledger_name=Lname,
            ledger_alias=Lalias,
            group_under=Lunder,
            ledger_opening_bal=Lopening_bal,
            ledger_type=typ_of_ledg,
            provide_banking_details=provide_banking,
        )
        Lmdl.save()
        idd = Lmdl
        Bmdl = Ledger_Banking_Details(
        
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
        M_mdl = Ledger_Mailing_Address(

            name=Mname,
            address=Maddress,
            state=Mstate,
            country=Mcountry,
            pincode=Mpincode,
        )
        M_mdl.save()
        T_mdl = Ledger_Tax_Register(
           
          
            gst_uin=Tgst_uin,
            register_type=Treg_typ,
            pan_no=Tpan_no,
            alter_gst_details=T_alter_gst,

        )
        T_mdl.save()
        LS_mdl = Ledger_Satutory(

            ledger_id=idd,
            assessable_calculation=assessable_calculationn,
            Appropriate_to =Appropriate_too ,
            gst_applicable=gst_applicablee,
            Set_alter_GST = Set_alter_GSTT,
            type_of_supply=type_of_supplyy,
            Method_of_calc = Method_of_calcc,


        )
        LS_mdl.save()

        rnd_mdl = Ledger_Rounding(
            ledger_id=idd,
            Rounding_Method=Rounding_Methodd,
            Round_limit =Round_limitt,

        )
        rnd_mdl.save()

        tax_mdl = ledger_tax(
            ledger_id=idd,
            type_of_duty_or_tax=type_of_duty_or_taxx,
            type_of_tax =type_of_taxx,
            valuation_type=valuation_typee,
            rate_per_unit=rate_per_unitt,
            Persentage_of_calculation=Persentage_of_calculationn,
        )
        tax_mdl.save()

        sndry_mdl = Ledger_sundry(
            ledger_id=idd,
            maintain_balance_bill_by_bill=maintain_balance_bill_by_billl,
            Default_credit_period=Default_credit_periodd,
            Check_for_credit_days =Check_for_credit_dayss,
        )
        sndry_mdl.save()
        messages.info(request,'LEDGER CREATED SUCCESSFULLY')
        return redirect('ledger.html')

def create_voucher(request):
    if request.method == 'POST':
        Vname = request.POST['nam']
        alias = request.POST['alias']
        vtype = request.POST['vtype']
        abbre = request.POST['abbre']
        activ_vou_typ = request.POST['avtyp']  # bool
        meth_vou_num = request.POST['meth_vou_num']
        useadv = request.POST.get('useadvc', False)
        prvtdp = request.POST.get('prvtdp', False)
        use_effct_date = request.POST['uefftdate']  # bool
        allow_zero_trans = request.POST['allow_zero_trans']  # bool
        allow_naration_in_vou = request.POST['allow_naration_in_vou']  # bool
        optional = request.POST['optional'] 
        provide_narr = request.POST['providenr']  # bool
        print = request.POST['print']  # bool

        if VoucherModels.objects.filter(voucher_name=Vname).exists():
                messages.info(request,'This Name is already taken...!')
                return render(request, 'load_create_vouchertyp')
        
        mdl = VoucherModels(

            voucher_name=Vname,
            alias=alias,
            voucher_type=vtype,
            abbreviation=abbre,
            active_this_voucher_type=activ_vou_typ,
            method_voucher_numbering=meth_vou_num,
            use_effective_date=use_effct_date,
            use_adv_conf = useadv,
            prvnt_duplictes =prvtdp,
            allow_zero_value_trns=allow_zero_trans,
            allow_naration_in_voucher=allow_naration_in_vou,
            make_optional=optional,
            provide_naration=provide_narr,
            print_voucher=print,

        )
        mdl.save()
        messages.info(request,'VOUCHER CREATED SUCCESSFULLY')
        return redirect('createvoucher')

    return render(request, 'createvoucher')


def currency(request):
    obj=CreateCurrency.objects.all()
    context={'cur':obj,}
    return render(request, 'currency.html',context)

def currency_alter(request,pk):
    cur=CreateCurrency.objects.get(id=pk)
    return render(request,'currency_alter.html',{'i':cur})
def load_create_currency(request):
    return render(request,'load_create_currency.html')

def create_currency(request):
    if request.method == 'POST':
        symbol = request.POST['symbol']
        fname = request.POST['fname']
        if len(symbol) <= 0:
            print('XX')
            return JsonResponse({
                'status': 00
            })
        elif len(fname) <= 0:
            print('XXX')
            return JsonResponse({
                'status': 00
            })
        else:
            pass

        iso_code = request.POST['iso_code']
        n_deci_placs = request.POST['n_deci_placs']
        smt_millon = request.POST['smt_millon']
        symbol_to_amount = request.POST['symbol_to_amount']
        space_bt_sy = request.POST['space_bt_sy']
        amount_after_decimal = request.POST['amount_after_decimal']
        amount_in_words = request.POST['amount_in_words']

        mdl_obj = CreateCurrency(
            symbol=symbol,
            formal_name=fname,
            ISO_code=iso_code,
            decimal_places=n_deci_placs,
            show_in_millions=smt_millon,
            suffix_to_amount=symbol_to_amount,
            space_symbol_amount=space_bt_sy,
            word_after_decimal=amount_after_decimal,
            decimal_no_in_words=amount_in_words,
        )
        mdl_obj.save()
        return redirect('currency')

def save_currency_data(request):
    if request.method == 'POST':
        sl = request.POST['slno']
        cname = request.POST['curname']
        stdr = request.POST['stdr']
        lvr = request.POST['lvr']
        sr = request.POST['sr']
        lvr2 = request.POST['lvr2']
        sr2 = request.POST['sr2']
        
        obj = CurrencyAlter(
            slno = sl,
            currencys= cname,
            stdrate = stdr,
            lastvrate = lvr,
            specirate = sr,
            lastvrate2 = lvr2,
            specirate2 = sr2,        
           
        )
        
        obj.save()
        grp = CreateCurrency.objects.all()
        obj1 = CurrencyAlter.objects.all()
        context = {'grp':grp ,'obj':obj1}
        return redirect('load_rates_of_exchange',context)

def update_currency(request,pk):
    if request.method=='POST':
        cur =CreateCurrency.objects.get(id=pk)
        cur.symbol = request.POST.get('symbol')
        cur.formal_name = request.POST.get('fname')
        cur.ISO_code = request.POST.get('iso_code')
        cur.decimal_places = request.POST.get('n_deci_placs')
        cur.show_in_millions = request.POST.get('smt_millon')
        cur.suffix_to_amount = request.POST.get('symbol_to_amount')
        cur.space_symbol_amount = request.POST.get('space_bt_sy')
        cur.word_after_decimal = request.POST.get('amount_after_decimal')
        cur.decimal_no_in_words = request.POST.get('amount_in_words')
        
        cur.save()
        return redirect('currency')
    return render(request, 'currency_alter.html',)

def stockgrpcreate(request):
    return render(request, 'stockgrpcreate.html')

def stockgrpscreate(request):
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        Should_quantties_of_items_be_added=request.POST['itemsadded']
        Set_or_Alter_GST_Details=request.POST['gst']
        data=stockgroupcreate(name=name,
                    alias=alias,
                    under=under,
                    itemsadded=Should_quantties_of_items_be_added,
                    gst=Set_or_Alter_GST_Details)
        data.save()
        messages.success(request,"Group added successfully!")
        
        return redirect('/')


def stock_grp(request):
    return render(request, 'stock_grp.html')



def stock_cat(request):
    return render(request, 'stock_cat.html')



def godwn(request):
    return render(request, 'gdwn.html')

def godwn_alter(request):
    return render(request, 'gdwn_alter.html')


def stock_items(request):
    sp=create_stockgrp.objects.all()
    std=create_stockcate.objects.all()
    pk=units.objects.all()
    return render(request,'stock_items.html',{'std':std,'pk':pk,'sp':sp})  



def add_stockitem(request):
     if request.method=='POST':
        lev=create_stockitem()
        lev.name=request.POST.get('name')
        lev.alias=request.POST.get('alias')
        lev.under=request.POST.get('under')
        lev.category=request.POST.get('cat')
        lev.units=request.POST.get('units')
        lev.rate_of_duty=request.POST.get('rate')
        lev.save()
        return redirect('stock_items')

def stockgrp(request):
    std=create_stockgrp.objects.all()
    return render(request,'stockgrpcreate.html',{'std':std}) 


def stockcate(request):
    return render(request,'stock_cat.html',)  


def add_stockcate(request):
    if request.method=='POST':
        name=request.POST['name']  
        alias=request.POST['alias']
        under=request.POST['under']
        std=create_stockcate(name=name,
                        alias=alias,
                        under=under,
                        )  

        std.save()     
        return redirect('stockcate')  
        # return render(request,'stockcategory.html')         

def add_stockgrp(request):
    if request.method=='POST':
        lev=create_stockgrp()
        lev.name=request.POST.get('name')
        lev.alias=request.POST.get('alias')
        lev.under=request.POST.get('under')
        lev.quntities_added=request.POST.get('qty')
        lev.save()
        return redirect('stockgrp') 

def stunits(request):
    ps=units()
    return render(request,'stunit.html',{'ps':ps}) 

def add_units(request):
    if request.method=='POST':
        std=units()
        std.type=request.POST.get('type')
        std.symbol=request.POST.get('symbol')  
        std.formal_name=request.POST.get('formal')
        std.number_of_decimal_places=request.POST.get('decimal') 
        std.first_unit=request.POST.get('ft')
        std.conversion=request.POST.get('con')
        std.second_unit=request.POST.get('sec')  
        std.save()
        return redirect('stunits')

def goddown(request):
    std=create_goddown.objects.all()
    return render(request,'goddown.html',{'std':std}) 

def add_goddown(request):
    if request.method =='POST':
        lev=create_goddown()
        lev.name=request.POST.get('name')
        lev.alias=request.POST.get('alias')
        lev.under=request.POST.get('under')
        lev.save()
        return redirect('goddown')
    return render(request,'goddown.html')   
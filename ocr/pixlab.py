import requests

# https://pixlab.io/cmd?id=ocr for additional information.


fields=responses&key=AIzaSyD-a9IF8KKYgoC3cpgS-Al7hLQDbugrDcw&alt=json
req = requests.get('https://content-vision.googleapis.com/v1/images:annotate', params={'img':'http://quotesten.com/wp-content/uploads/2016/06/Confucius-Quote.jpg', 'key': 'Message Structure', 'alt' : 'json'})
reply = req.json()
if reply['status'] != 200:
    print(reply['error'])
else:
    print("Input language: " + reply['lang'])
    print("Text Output: " + reply['output'])

    "For Internal Use Only" \
    "\nMorgan Stanley" \
    "\nBranch No.\nAccount No.\
    nFA/PWA No." \
    "\n0 1 0 99 462" \
    "\nAccount Transfer Form Clearing Number: 0015" \
    "\nce. acc" \
    "\nPlease use a separate fo. for each account u are ransfo ig. Please attach a copy of your" \
    "\nA. To Be Completed By The Branch\nAc Type (Please check one)" \
    "\nenemiering team. Berlin on Bain\nVIP Money Purchase or Profit Sharing Plan" \
    "\nType (Please ck one)\nV AO\nad page\nB. " \
    "Information About Your Morgan Stanley Account (Required)\nROBIN VARGHESE ROBIN K SECONDARY TEN COM" \
    "\n101-099462-012\nON FILE\nACCOUNT TITLE\nACCOUNT NUMBER/FA OR PWA NUMBER" \
    "\nSOCIAL SECURITY OR TAXPAYER ID NUMBER\nC. Information About The Account You Are Transferring (Required)" \
    "\nSTEPHENS INC.\n0419\nCARRYING ORGANIZATION\nCLEARING NUMBER\nSTREET ADDRESS (PLEASE INCLUDE CITYSTATE AND ZIP CODE." \
    "\nROBIN VARGHESE ROBIN K SECONDARY TEN COM\n12346578\nACCOUNT TITLE\nACCOUNT NUMBER" \
    "\nD. Brokerage, Mutual Fund, Annuities or Bank Securities Transfer (Required — Please choose Either box 1, 2, 3 or 4)" \
    "\n-Kind (Ple sferable ACATS. The Morgan Stanley Fi Adh Wealth\nAdvisor ontact Morgan Stanley Insurai ce Opera 1s at 800-490-5412 iate the annuity transfer p" \
    "\n2. iquidate all sts and sfer p Check Wire transfe ly be ed) (Pleas -Morgan Stanley does not guara" \
    "\nif the de Ug fir iquidat Therefo rd that yo iquidate assets at deli rg fir and th. this form by sele\noption 1. " \
    "\"I wish to ran1sfer my entire account In-Kind to ve the cash proceeds transferred.)\nO Partial Tran transfe -Kind iquids and transfer proceeds for only th :d be (Ple Ittach addi al sheet if, ary)" \
    "\nof A Symbol or CUSIP of S Type of Tr\nKind O Liquidate\nKind\nLiquidate\nD For CD Transfers ONLY (Plea check one)" \
    "\nLiquid ity (M ity D.\nLiquid Imme of and ack\nit d\n(MMIDDIYY) (PI\nedge the pe\n2-3 eks p!\nthd\nUnt and transfer" \
    "\nDELIVERING BROKER: Refer to page Lctions, Subject le by-la and les of the N.S.C.C.\nE. Please Read carefully And Sign This Section" \
    "\nTo the organization named in Section C above:\nIf this accoul ified reme accou and the delivering fit ustee or c todian of the plan have a ended the applicable plan so that es Morgan St" \
    "\nBarney LLC sfer all Morgan S id th:\ne exte any asse in my accou are not readily transferable, with or without penalties such asse may not be transferred within time frame required by NYSE Rule" \
    "\n412 of the FINRA other design 1g auth\nUnless otherwise indicated in the instructions above, I authorize you to liquidate any sferable proprietary rket fund assets that are pa of my" \
    "\n1g credit b. Morgan St ded standing fees due you fr the credit b; If my" \
    "\nbalance, or if the credit balance insufficient to satis sfy any ot tanding fees due you, authorize you to liquidate the asset in my account to the extent necessary to satis sfy that obligation." \
    "\nid that if I ch ethod of dispo other ti iquida id transfe ly be able for the payi\npenal th respect to such asse\ndial change ry of the be changed Morgan St ey C/F By changing" \
    "\nMorgan St of my derstand and agr The change of be processed as a trus" \
    "\n2) All further requests for service to this contract require an authorization from Morgan Stanley, 3) All proceeds from this contract be deposited directly into my\nad 4) The beneficiary ontract will be ed as Morgan Stanley as th\nund you wi Ict me respect he dispos ion of any asset in my accout are no transferable. If certificat or other ume my accout" \
    "\nphysical pe sfer th good de able fo ding affixing any able Morgan Stanley" \
    "\nthem in its name for the purp of sal when and as directed by me" \
    "\nI understand that upon rec opy of thi rders fo books. I als\nedit/debit card; sed checks issued to me if any lection with my securities account" \
    "\nF. Client Consent to Cash Sweep Program\nig free credit balk\nlances in my acc Morgan Stanley ep progr th any Morgan St" \
    "\nFinancial Advisor understand that the Morgan Stanley cash sweep program automatically invests any free credit balances in my account in my designated sweep investment option." \
    "\nif any of my igible, Morgan St further di ly depe ep all\nfree credit balances to one or more FDIC sured depos tory tutio \"Sweep Banks" \
    "\") affiliated with Morgan Stanley up to $2,000,000 and ther to a honey market\nmutual fund as more particularl the B; Dep Prog “Bank Depo Prog ilabl" \
    "\nealth/services/bankdepe programasp and up the depa the Bank Dep Program, an ad by be b edge and" \
    "\nad that Morgan St d the of S ep Banks th 30 days pt ACCOUNT TRANSFER FORM CLEARING NUMBER: 0015\n(O8/2016) ATSATFF\n1\n1313\nPAGE 1 OF 2\nNY CS 8575959 08/16\nATSATFF\nBWF\n",


    $.ajax({
        type: 'POST',
        url: '/processtext',
        data: JSON.stringify({"data": data}),
        contentType: 'application/json',
        success: function(response) {
        console.log(response);
    },
    error: function(error)
    {
        console.log(error);
    }
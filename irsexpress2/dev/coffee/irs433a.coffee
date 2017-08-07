'use strict'
$ ->
    # 433a-form-specific-only actions

    form433a_page = $('.433A-pageactive').data('value')

    # --------------------------------------------------------------------------
    # PAGE 4
    if form433a_page == 'is_page4_active'
        # page 4 - specific actions
        $(document).on "keyup", ".form433a .account_balance", () ->
            sum = 0
            $(".form433a .account_balance").each ->
                sum += myparseInt($(this).val())
                return true
            $(".form433a #id_total_cash").val(sum).keyup()

        $(document).on "keyup", ".form433a .loan_balance_curval", () ->
            lb = cv = 0
            $(".form433a .loan_balance").each ->
                lb += myparseInt($(this).val())
                return true
            $(".form433a .current_value").each ->
                cv += myparseInt($(this).val())
                return true
            equity = cv - lb
            $(".form433a #id_total_equity").val(equity).keyup()

        $(document).on "keyup", ".form433a .amount_owed_crlimit", () ->
            ao = cl = 0
            $(".form433a .amount_owed").each ->
                ao += myparseInt($(this).val())
                return true
            $(".form433a .credit_limit").each ->
                cl += myparseInt($(this).val())
                return true
            total_credit = cl - ao
            $(".form433a #id_total_credit").val(total_credit).keyup()

        $(document).on "keyup", ".form433a .cash_value_lbal", () ->
            lb = cv = 0
            $(".form433a .iiloan_balance").each ->
                lb += myparseInt($(this).val())
                return true
            $(".form433a .cash_value").each ->
                cv += myparseInt($(this).val())
                return true
            acash = cv - lb
            $(".form433a #id_total_available_cash").val(acash).keyup()

    # --------------------------------------------------------------------------
    # PAGE 5
    if form433a_page == 'is_page5_active'
        # page 5 - specific actions
        $(document).on "keyup", ".form433a .rpfmv_clb", () ->
            lb = mv = 0
            $(".form433a .rpcurrent_loan_balance").each ->
                lb += myparseInt($(this).val())
                return true
            $(".form433a .rpmarket_value").each ->
                mv += myparseInt($(this).val())
                return true
            equity = mv - lb
            $(".form433a #id_real_property_total_equity").val(equity).keyup()

        $(document).on "keyup", ".form433a .vvfmv_clb", () ->
            lb = mv = 0
            $(".form433a .vvcurrent_loan_balance").each ->
                lb += myparseInt($(this).val())
                return true
            $(".form433a .vvmarket_value").each ->
                mv += myparseInt($(this).val())
                return true
            equity = mv - lb
            $(".form433a #id_vehicles_total_equity").val(equity).keyup()

        $(document).on "keyup", ".form433a .pafmv_clb", () ->
            lb = mv = 0
            $(".form433a .pacurrent_loan_balance").each ->
                lb += myparseInt($(this).val())
                return true
            $(".form433a .pamarket_value").each ->
                mv += myparseInt($(this).val())
                return true
            equity = mv - lb
            $(".form433a #id_personal_assets_total_equity").val(equity).keyup()
        
        # REQ: Do you have any other personal assets? - can we have a checkbox to enter home address?
        $(document).on "click", ".form433a .pa-sethomeaddress", () ->
            this_tr = $(this).closest('tr')
            hldata = $('.formelement-home_location input', this_tr).val()
            hldata = JSON.parse(hldata)
            for fk, value of hldata
                if fk in ['location_county', 'location_state_name']
                    elem = $(".formelement-#{fk} select", this_tr)
                else
                    elem = $(".formelement-#{fk} input", this_tr)
                if elem.length > 0
                    $(elem).val(value).trigger('change')
            # window.form_saved = false
            return false

    # --------------------------------------------------------------------------
    # PAGE 6
    if form433a_page == 'is_page6_active'
        # page 6 - specific actions
        # see Page6EditView.get_context_data() for explanations
        suggestions = $('.irs-suggestions-data').html()
        suggestions = JSON.parse(suggestions)
        for sugg in suggestions
            element = $(sugg['element-selector'])
            data = '<p class="sugg"><span class="' + sugg['class'] + '">IRS Express suggests: <span class="value">' + sugg['value'] + '</span></span><span class="desc">' + sugg['desc'] + '</span></p>'
            $(data).insertAfter(element)

        window.calc_expenses = () ->
            income = expense = 0
            # console.log "inpfld"
            $(".form433a .income_field").each ->
                if $(this).attr('id') == 'id_net_business_income'
                    hval = $(this).html().replace(/[\<\>span\s\$\/]/g, '')
                    income += myparseInt(hval)
                else
                    income += myparseInt($(this).val())
                return true
            $(".form433a .expense_field").each ->
                expense += myparseInt($(this).val())
                return true
            $(".form433a #id_total_income_cnt span").html(income).keyup()
            $(".form433a #id_total_expenses_cnt span").html(expense).keyup()
            netdiff = income - expense
            # if netdiff < 0
            #     netdiff = 0
            $(".form433a #id_net_difference_cnt span").html(netdiff).keyup()

        $(document).on "keyup", ".form433a .inpfld", () ->
            calc_expenses()
        calc_expenses()
        mask_num(".form433a #id_net_business_income span")
        mask_num(".form433a #id_total_income_cnt span")
        mask_num(".form433a #id_total_expenses_cnt span")
        mask_num(".form433a #id_net_difference_cnt span")

    # --------------------------------------------------------------------------
    # PAGE 7
    if form433a_page == 'is_page7_active'
        # page 7 - specific actions
        window.hide_page7_elements = () ->
            $('.form433a-page-7 > table > tbody > tr').each ->
                this_tr = $(this)
                if $('input[name="is_self_employed"]', this_tr).length > 0
                    # skip first row
                    return true
                this_tr.hide()
                return true

        window.show_page7_elements = () ->
            $('.form433a-page-7 > table > tbody > tr').each ->
                this_tr = $(this)
                if $('input[name="is_self_employed"]', this_tr).length > 0
                    # skip first row
                    return true
                this_tr.show()
                return true
            # kind of hardcode - re-hide items
            if not $('.form433a input[name="has_bank_account"]').data("bootstrap-switch").state()
                $('.showhidewith-chk-businessbankacc').closest('tr.fieldrow').hide()
            if not $('.form433a input[name="has_accounts_receivable"]').data("bootstrap-switch").state()
                $('.showhidewith-chk-accountsreceivable').closest('tr.fieldrow').hide()
            if not $('.form433a input[name="has_business_assets"]').data("bootstrap-switch").state()
                $('.showhidewith-chk-businessasset').closest('tr.fieldrow').hide()

        $('.form433a input[name="is_self_employed"]').on 'switchChange.bootstrapSwitch', (event, state) ->
            if state
                this_tr = $(this).closest('tr')
                show_page7_elements()
            else
                hide_page7_elements()
            return true

        if not $('.form433a input[name="is_self_employed"]').data("bootstrap-switch").state()
            hide_page7_elements()

        $(document).on "keyup", ".form433a .bba_account_balance", () ->
            cbnk = 0
            $(".form433a .bba_account_balance").each ->
                cbnk += myparseInt($(this).val())
                return true
            $(".form433a #id_total_cash_in_banks").val(cbnk).keyup()

        $(document).on "keyup", ".form433a .ar_amount_due", () ->
            arad = 0
            $(".form433a .ar_amount_due").each ->
                arad += myparseInt($(this).val())
                return true
            $(".form433a #id_outstanding_balance").val(arad).keyup()

        $(document).on "keyup", ".form433a .bafmv_clb", () ->
            lb = mv = 0
            $(".form433a .bacurrent_loan_balance").each ->
                lb += myparseInt($(this).val())
                return true
            $(".form433a .bamarket_value").each ->
                mv += myparseInt($(this).val())
                return true
            equity = mv - lb
            $(".form433a #id_total_equity").val(equity).keyup()

        # REQ: For the Do you have business assets?, please have a checkbox to
        # automatically enter the business address for each of the Business Assets
        $(document).on "click", ".form433a .pa-setbusinessaddress", () ->
            this_tr = $(this).closest('tr')
            locnames = ['street', 'city', 'state_name', 'zipcode', 'county']
            for lname in locnames
                if lname in ['county', 'state_name']
                    elem = $(".formelement-location_#{lname} select", this_tr)
                else
                    elem = $(".formelement-location_#{lname} input", this_tr)
                bselem = $("#id_business_#{lname}")
                if elem.length > 0 and bselem.length > 0
                    console.log("Set #{lname}")
                    $(elem).val($(bselem).val()).trigger('change')
                else
                    console.log("Cannot set #{lname}")
            return false

    # --------------------------------------------------------------------------
    # PAGE 8
    if form433a_page == 'is_page8_active'
        # page 8 - specific actions

        window.calc_expenses = () ->
            income = expense = 0
            # console.log "inpfld"
            $(".form433a .income_field").each ->
                income += myparseInt($(this).val())
                return true
            $(".form433a .expense_field").each ->
                expense += myparseInt($(this).val())
                return true
            $(".form433a #id_total_income_cnt span").html(income).keyup()
            $(".form433a #id_total_expenses_cnt span").html(expense).keyup()
            netdiff = income - expense
            $(".form433a #id_net_difference_cnt span").html(netdiff).keyup()

        $(document).on "keyup", ".form433a .inpfld", () ->
            calc_expenses()
        mask_num(".form433a #id_total_income_cnt span")
        mask_num(".form433a #id_total_expenses_cnt span")
        mask_num(".form433a #id_net_difference_cnt span")
        calc_expenses()

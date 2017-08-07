'use strict'
$ ->
    monthNames = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]

    $('#oic_calc_btn').click ->
        elemid = $(this).data('id')
        # console.log("clicked #{elemid}")
        url = $(this).data('sourceurl')
        if $('#object_data.client-id').length > 0
            client_id = $('#object_data.client-id').data('objectid')
            url = "#{url}#{client_id}"
        modalform = $(".modal-element")
        $.ajax url,
            type: 'GET'
            dataType: 'html'
            success: (data, textStatus, jqXHR) ->
                $(modalform).html(data)
                reinitWidgets()
                $('.modalform', modalform).modal show: true,
                    keyboard: true
                $('.modal .formsavebtn', modalform).click ->
                    # $('form', modalform).submit()
                    $('form', modalform).ajaxSubmit()
                    $('.modalform', modalform).modal('hide')
                oic_calculator()
                return false
        return false

    window.oic_calculator = () ->
        console.log "oic_calculator"
        admonth = myparseInt($('#id_pp_assessed_date_month').val()) - 1
        adday = myparseInt($('#id_pp_assessed_date_day').val())
        adyear = myparseInt($('#id_pp_assessed_date_year').val())
        if admonth == 0 or adday == 0 or adyear == 0
            $('.pp-calculation').hide()
        else
            expdate = new Date(adyear + 10, admonth, adday)
            nowtime = new Date()
            months = ((expdate - nowtime)/(1000*60*60*24*30.44)).toFixed()
            $('#pp_statute_exp_date').html("#{admonth + 1}-#{adday}-#{adyear + 10}")
            $('#pp_statute_months_avail').html("#{months} months")
            income = myparseInt($('#id_pp_monthly_income').val())
            debt = myparseInt($('#id_pp_debt_total').val())
            can_pay = months * income
            $('#pp_can_pay').html("#{can_pay}").keyup()
            if can_pay < debt
                $('#pp_suggestion_qualify').html('MAY be')
            else
                $('#pp_suggestion_qualify').html('NOT')
            sugg_amount = income * 12
            $('#pp_suggested_amount').html("#{sugg_amount}").keyup()
            oamount = myparseInt($('#id_pp_offer_amount').val())
            $('#id_pp_offer_amount').val(sugg_amount).keyup()
            $('.pp-calculation').show()
        oic_calculator2()
        return true

    window.oic_calculator2 = () ->
        oamount = myparseInt($('#id_pp_offer_amount').val())
        console.log "oic_calculator2, oamount: #{oamount}"
        if not oamount or oamount == 0
            $('.pp-calculation2').hide()
        else
            initial_payment = (oamount / 5).toFixed()
            $('#pp_initial_payment').html(initial_payment).keyup()
            remaining_balance = oamount - initial_payment
            cnt = 6
            for i in [1..5]
                value = (remaining_balance / (cnt - i)).toFixed()
                remaining_balance = remaining_balance - value
                $("#pp_payment_#{i}").html(value).keyup()
            $('.pp-calculation2').show()
        return true

    $(document).on 'keyup', '.oic-calculator input', () ->
        oic_calculator()
    $(document).on 'change', '.oic-calculator input', () ->
        oic_calculator()
    $(document).on 'change', '.oic-calculator select', () ->
        oic_calculator()
    $(document).on 'keyup', '#id_pp_offer_amount', () ->
        oic_calculator2()
    $(document).on 'change', '#id_pp_offer_amount', () ->
        oic_calculator2()

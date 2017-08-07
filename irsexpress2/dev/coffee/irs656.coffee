'use strict'
$ ->
    # 656-form-specific-only actions

    form656_page = $('.656-pageactive').data('value')
    monthNames = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]

    # --------------------------------------------------------------------------
    # PAGE 5
    if form656_page == 'is_page5_active'
        # page 5 - specific actions
        window.f656page5_recalc_lumpsum = () ->
            admonth = myparseInt($('#id_assessed_date_month').val()) - 1
            adday = myparseInt($('#id_assessed_date_day').val())
            adyear = myparseInt($('#id_assessed_date_year').val())
            if admonth == 0 or adday == 0 or adyear == 0
                $('#id_statute_exp_date').html('-')
                $('#id_statute_months_avail').html('-')
                $('#lumpsum_decision').html('probably may be')
                $('#id_suggested_amount span').html('0').keyup()
                $('#id_can_pay span').html("0").keyup()
            else
                expdate = new Date(adyear + 10, admonth, adday)
                nowtime = new Date()
                months = ((expdate - nowtime)/(1000*60*60*24*30.44)).toFixed()
                $('#id_statute_exp_date').html("#{monthNames[admonth]}/#{adday}/#{adyear + 10}")
                $('#id_statute_months_avail').html("#{months} months")
                income = myparseInt($('#id_monthly_income').val())
                debt = myparseInt($('#id_debt_total').val())
                can_pay = months * income
                $('#id_can_pay span').html("#{can_pay}").keyup()
                if can_pay < debt
                    $('#lumpsum_decision').html('MAY be')
                else
                    $('#lumpsum_decision').html('NOT')
                $('#id_suggested_amount span').html("#{income * 12}").keyup()
                offer_amount = myparseInt($('#id_offer_amount_lumpsum').val())
                initial_payment = myparseInt($('#id_initial_payment').val())
                payment_1 = myparseInt($('#id_payment_1').val())
                payment_2 = myparseInt($('#id_payment_2').val())
                payment_3 = myparseInt($('#id_payment_3').val())
                payment_4 = myparseInt($('#id_payment_4').val())
                payment_5 = myparseInt($('#id_payment_5').val())
                if offer_amount == 0 or not window.offer_amount_changed
                    offer_amount = income * 12
                    $('#id_offer_amount_lumpsum').val(offer_amount).keyup()
                    mark_unsaved()
                if initial_payment == 0 or not window.initial_payment_changed
                    initial_payment = (offer_amount / 5).toFixed()
                    $('#id_initial_payment').val(initial_payment).keyup()
                    mark_unsaved()
                remaining_balance = offer_amount - initial_payment
                $('#id_remaining_balance span').html(remaining_balance).keyup()
                rem = remaining_balance
                cnt = 6
                for i in [1..5]
                    # rem = rem - remaining_balance / 5
                    value = (rem / (cnt - i)).toFixed()
                    rem = rem - value
                    $("#payment_#{i}_advice span.field-number").html(value).keyup()
                    if not window.payments_changed[i]
                        $("#id_payment_#{i}").val(value).keyup()

        # we can auto-calculate the values only if they were empty in the beginning
        # if the user changes them - lets keep
        offer_amount = myparseInt($('#id_offer_amount_lumpsum').val())
        initial_payment = myparseInt($('#id_initial_payment').val())
        window.offer_amount_changed = offer_amount > 0
        window.initial_payment_changed = initial_payment > 0
        window.payments_changed = [false, false, false, false, false]

        for i in [1..5]
            payment_val = myparseInt($("#id_payment_#{i}").val())
            window.payments_changed[i] = payment_val > 0
            # w = myparseInt($("#id_payment_#{i}").css('width'))
            # console.log "width: #{w}, w/2: #{w/2}"
            $("#id_payment_#{i}").css('width', 200).css('display', 'inline')
            $('<span id="payment_'+i+'_advice" data-pi="'+i+'" class="payment_advice"><span class="fa fa-arrow-left"></span> $ <span class="field-number">0</span></span>').insertAfter("#id_payment_#{i}")

        $(document).on 'click', '.payment_advice', () ->
            v = $('span.field-number', this).html()
            thistr = $(this).closest('tr')
            $('input', thistr).val(v).keyup()
            pi = $(this).data('pi')
            window.payments_changed[pi] = false

        f656page5_recalc_lumpsum()
        $('.formelement-assessed_date').on 'change', 'select', () ->
            f656page5_recalc_lumpsum()
        $('#id_monthly_income').on 'change', () ->
            f656page5_recalc_lumpsum()
        $('#id_debt_total').on 'change', () ->
            f656page5_recalc_lumpsum()
        $('#id_offer_amount_lumpsum').on 'change', () ->
            window.offer_amount_changed = true
            f656page5_recalc_lumpsum()
        $('#id_initial_payment').on 'change', () ->
            window.initial_payment_changed = true
            f656page5_recalc_lumpsum()

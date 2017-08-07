'use strict'
$ ->
    # only for IRS form pages
    if $('form#pageform .irsform').length > 0
        # ----------
        window.disable_switch = false
        # processing 1x1 subforms
        # show_1x1_subform() - shows a sub form in 1-to-1 relation
        window.show_1x1_subform = (prev, src_url, unlock_name) ->
            # src_url = $(url_selector).data('url')
            if not src_url
                console.exception "1x1 subform: src_url is empty!"
                return false
            $.ajax src_url,
                type: 'GET'
                dataType: 'html'
                success: (data, textStatus, jqXHR) ->
                    $(data).insertAfter(prev)
                    reinitWidgets()
                    if unlock_name
                        content_loaded(unlock_name)
                    return false

        # toggle 1-to-1 subform
        $('.irsform input.form1x1switcher').on 'switchChange.bootstrapSwitch', (event, state) ->
            if window.disable_switch
                return true
            window.disable_switch = true
            subformname = $(this).data('subform-name')
            src_url = $("##{subformname}_form_url").data('url')
            subform_selector = $("##{subformname}_form_url").data('subform-selector')
            if state
                this_tr = $(this).closest('tr')
                show_1x1_subform(this_tr, src_url)
            else
                if not confirm("This action will remove the section below. Are you sure?")
                    window.disable_switch = true
                    $(this).data("bootstrap-switch").state(true)
                    window.disable_switch = false
                    return true
                $(this).data("bootstrap-switch").state(false)
                $(subform_selector).remove()
            window.disable_switch = false
            return true

        # initial status
        if $('.irsform input.form1x1switcher').length > 0
            $('.irsform input.form1x1switcher').each ->
                subformname = $(this).data('subform-name')
                src_url = $("##{subformname}_form_url").data('url')
                if $(this).data("bootstrap-switch").state()
                    waitload_list[subformname] = true
                    this_tr = $(this).closest('tr')
                    show_1x1_subform(this_tr, src_url, subformname)
                return true

        # ----------
        # adjust calculations for sub-blocks
        window.adjust_calculations = () ->
            $('.form433a-page-4 input.number-field').keyup()
            $('.form433a-page-5 input.number-field').keyup()
            $('.form433a-page-7 input.number-field').keyup()

        # processing 1xN subforms
        window.subforms_1xn_counts = {}
        window.subforms_1xn_maxcounts = {}
        window.add_1xn_subform = (prev, src_url, subformname, unlock_name) ->
            if not src_url
                console.exception "1xn subform: src_url is empty!"
                return false
            maxcnt = window.subforms_1xn_maxcounts[subformname]
            cnt = window.subforms_1xn_counts[subformname]
            if maxcnt > 0 and cnt == maxcnt
                alert "Allowed only #{maxcnt} items"
                return false
            src_url = $("##{subformname}_form_url").data('url')
            window.subforms_1xn_counts[subformname] += 1
            cnt = window.subforms_1xn_counts[subformname]
            $.ajax "#{src_url}#{subformname}_#{cnt}",
                type: 'GET'
                dataType: 'html'
                success: (data, textStatus, jqXHR) ->
                    $(data).insertAfter(prev)
                    reinitWidgets()
                    adjust_calculations()
                    if unlock_name
                        content_loaded(unlock_name)
            return false

        window.toggle1xNformset = (element, managed) ->
            subformname = $(element).data('subform-name')
            state = $(element).data("bootstrap-switch").state()
            if state
                this_tr = $(element).closest('tr')
                window.subforms_1xn_counts[subformname] = 0
                src_url = $("##{subformname}_form_url").data('url')
                add_1xn_subform(this_tr, src_url, subformname)
                $('.showhidewith-chk-' + subformname).closest('tr.fieldrow').show()
            else
                if managed
                    if not confirm("This action will remove the section below. Are you sure?")
                        window.disable_switch = true
                        $(element).data("bootstrap-switch").state(true)
                        window.disable_switch = false
                        return false
                dsse = window.disable_switch
                window.disable_switch = true
                $(element).data("bootstrap-switch").state(false)
                window.disable_switch = dsse
                selector = $("##{subformname}_form_url").data('subform-selector')
                $(selector).remove()
                window.subforms_1xn_counts[subformname] = 0
                $('.showhidewith-chk-' + subformname).closest('tr.fieldrow').hide()
            return true

        # toggle 1xN form
        $('.irsform input.form1xnswitcher').on 'switchChange.bootstrapSwitch', (event, state) ->
            if window.disable_switch
                return true
            window.disable_switch = true
            toggle1xNformset($(this), true)
            window.disable_switch = false
            return true

        # button "Add New"
        $('form#pageform').on "click", ".add-subform", () ->
            this_tr = $(this).closest('tr')
            subformclassname = $(this_tr).data('subform-classname')
            subformname = $('*[data-subform-selector=".' + subformclassname + '"]').data('subform-name')
            src_url = $("##{subformname}_form_url").data('url')
            add_1xn_subform(this_tr, src_url, subformname)
            return false

        # button "Remove"
        $('form#pageform').on "click", ".remove-subform", () ->
            this_tr = $(this).closest('tr')
            subformclassname = $(this_tr).data('subform-classname')
            subformname = $('*[data-subform-selector=".' + subformclassname + '"]').data('subform-name')
            $(this_tr).remove()
            adjust_calculations()
            # if no dependents shown - uncheck the checkbox
            if $(".#{subformclassname}").length == 0
                window.disable_switch = true
                switcher = $(".irsform input.form1xnswitcher.switcher-#{subformname}")
                switcher.data("bootstrap-switch").state(false)
                toggle1xNformset(switcher, false)
                window.disable_switch = false
                # $(".irsform input.form1xnswitcher.switcher-bankaccount")
                $('.showhidewith-chk-' + subformname).closest('tr.fieldrow').hide()
            return false

        # Initial status
        if $('.irsform input.form1xnswitcher').length > 0
            $('.irsform input.form1xnswitcher').each ->
                subformname = $(this).data('subform-name')
                # console.log "subformname: #{subformname}"
                subform_cnt = $(this).data('subform-count')
                subform_maxcnt = $(this).data('subform-maxcount')
                window.subforms_1xn_counts[subformname] = 0
                window.subforms_1xn_maxcounts[subformname] = subform_maxcnt
                if subform_cnt > 0
                    src_url = $("##{subformname}_form_url").data('url')
                    this_tr = $(this).closest('tr')
                    $(this).data("bootstrap-switch").state(true)
                    for x in [1...subform_cnt]
                        waitload_list["#{subformname}_#{x}"] = true
                        add_1xn_subform(this_tr, src_url, subformname, "#{subformname}_#{x}")
                    $('.showhidewith-chk-' + subformname).closest('tr.fieldrow').show()
                else
                    $('.showhidewith-chk-' + subformname).closest('tr.fieldrow').hide()
                return true

        # ------------------------------------------
        # radiogroups
        $(document).on 'switchChange.bootstrapSwitch', '.chk-radiogroup', (event, state) ->
            deptrs = $(this).data('dep_rows').split ' '
            for deptr in deptrs
                trelem = $(".formelement-#{deptr}").closest('tr')
                if state
                    trelem.removeClass('hidden')
                    $("#id_#{deptr}").removeClass('hidden')
                else
                    if not trelem.hasClass('hidden')
                        trelem.addClass('hidden')

        # disable control if has class 'disabled' - just initial state
        if $('.toggle-chkbox.disabled').length > 0
            $('.toggle-chkbox.disabled').data("bootstrap-switch").disabled(true)

        # --------------------------------------------------------------------------
        # FORM SAVE
        # --------------------------------------------------------------------------
        window.mark_unsaved = (element) ->
            if window.form_saved
                window.form_saved = false
                $('.form_save_page').removeClass('hidden')
                $('div#formaffix').removeClass('hidden')

        window.mark_saved = () ->
            if not window.form_saved
                window.form_saved = true
                $('.form_save_page').addClass('hidden')
                $('div#formaffix').addClass('hidden')

        # initial value: saved if form has id
        formid = $('input[name="id"]').val()
        if formid
            window.form_saved = false
            mark_saved()
        else
            window.form_saved = true
            mark_unsaved()

        # indicator whether the form has changed
        $('form#pageform').on 'change', '.irsform input, .irsform select, .irsform textarea', () ->
            elem = $(this)
            # console.log "Element changed: #{elem.attr('id')}"
            mark_unsaved(elem)
            true

        # $('.irsform input.toggle-chkbox').on 'switchChange.bootstrapSwitch', (event, state) ->
        $('form#pageform').on 'switchChange.bootstrapSwitch', '.irsform input.toggle-chkbox', (event, state) ->
            elem = $(this)
            # console.log "Element changed: #{elem.attr('id')}"
            mark_unsaved(elem)
            true

        # on form submit - validate child entities by ajax and mark errors
        window.submit_irs_form = (next_page, save) ->
            # window.validating_form = "#pageform"
            window.validating_form = ""
            form_selector = "#pageform"
            # validate main form
            form_data = {}
            form_data['do_form_save'] = save
            form_name = 'mainform'
            ecount = 0
            process_elements = (elements) ->
                elements.each ->
                    name = $(this).attr('name')
                    type = $(this).attr('type')
                    value = $(this).val()
                    if type == 'checkbox'
                        value = $(this).data("bootstrap-switch").state()
                    # console.log("processing #{name}: #{value}")
                    form_data[name] = value
                    return true
            all_inputs = $("#{form_selector} input")
            all_selects = $("#{form_selector} select")
            all_textareas = $("#{form_selector} textarea")
            v = process_elements(all_inputs)
            v = process_elements(all_selects)
            v = process_elements(all_textareas)
            # 'virtual' field on page6
            if form443a_page? and form443a_page == 'is_page6_active'
                form_data['net_business_income'] = 0
            src_url = $(window.validating_form).attr('action')
            $.ajax src_url,
                type: 'POST'
                dataType: 'html'
                data: $.param(form_data)
                success: (data, textStatus, jqXHR) ->
                    # console.log "response: #{data}"
                    $('ul.errorlist').remove()
                    if data != 'OK'
                        jsdata = JSON.parse(data)
                        for errors in jsdata
                            fieldname = errors[0]
                            errorlist = errors[1]
                            errortxt = '<ul class="errorlist">'
                            for etxt in errorlist
                                errortxt += "<li>#{etxt}</li>"
                            errortxt += '</ul>'
                            $(errortxt).insertAfter('label[for*="id_' + fieldname + '"]')
                        # reinitWidgets()
                        form_validated(form_name, 2)
                        alert("Some fields are filled incorrectly.\nPlease fix issues and submit the form again.")
                    else
                        form_validated(form_name, 0)
                        if save
                            mark_saved()
                            # if we have not saved instances - reload page to get them
                            if $('.form-id[value=""]').length > 0 and not next_page
                                next_page = window.location.href
                        if next_page
                            window.location.href = next_page
                            return false
                        # alert("Data saved")
                        return true
                    return false
            return false

        $(document).on "click", ".irsform-form-save", () ->
            next_page = $(this).data('url')
            submit_irs_form(next_page, true)
            return false

        # Trying to handle form leaving
        window.onbeforeunload = () ->
            if window.form_saved
                return undefined
            submit_irs_form(null, false)
            # return 'Are you sure you want to leave?'
            return ' '

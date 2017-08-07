'use strict'
$ ->

    window.pass = () ->
        # does nothing, just a stub
        return false

    window.myparseInt = (value) ->
        val = parseInt(value.replace(/[\.,]/g, ''))
        return val

    # kind of waiting queue - do not show some content unless all loaded
    window.waitload_list = {}
    window.content_loaded = (name) ->
        if name
            console.log "#{name} loaded"
            waitload_list[name] = false
        all_loaded = true
        for item, notloaded of waitload_list
            if notloaded
                console.log "waiting for #{item} to be loaded"
                all_loaded = false
                break
        if all_loaded
            $('.content-load-wait').each ->
                celem = $(this).data('content-element')
                if celem
                    $(celem).removeClass('hidden')
                reinitWidgets()
                $(this).hide()
        return false

    # kind of form validation queue - do not post form until all processed
    # contains elements with values:
    # 0: validation success
    # 1: validation in progress
    # 2: validation failed - need to show errors
    window.waitvalidation_list = {}
    window.validating_form = ""
    window.form_validated = (name, result) ->
        if name
            console.log "form #{name} validated (#{result})"
            waitvalidation_list[name] = result
        all_validated = true
        for item, validation_state of waitvalidation_list
            if validation_state == 1
                console.log "waiting for #{item} to be validated"
                all_validated = false
                break
            if validation_state == 2
                # show errors
                console.log "form #{item} validation failed"
                all_validated = false
                $('.form-validation-wait').hide()
                break
        if all_validated and window.validating_form.length > 0
            console.log "submitting form"
            $(window.validating_form).submit()
            return true

    window.reinitWidgets = () ->
        # if window.getSelection()
        #     window.getSelection().removeAllRanges()
        # else if document.selection
        #     document.selection.empty()
        $('.toggle-chkbox').bootstrapSwitch()
        $('.switch-radio2').bootstrapSwitch()
        # init select2
        $('select').select2()
        $('.xtooltip').tooltip()
        $('[data-toggle="popover"]').popover()

    $('.img-popover').popover
        trigger: 'hover',
        placement: 'right',
        content: () ->
            '<img src="' + $(this).data('src') + '">'
        ,
        title: "",
        html: true

    reinitWidgets()

    $('.form-group').each ->
        error_messages = $(this).attr('error_messages')
        if error_messages
            $(this).addClass('has-error')
            $('input', this).popover
                placement: 'right',
                content: () ->
                    '<span class="text-danger">' + error_messages + '</span>'
                ,
                title: "",
                html: true
            $('input', this).popover('show')

    set_scrollable = ->
        window_height = $(document).height()
        content_height = window_height - 300
        $('.scrollable').height(content_height)

    $(window).resize(set_scrollable)
    set_scrollable()

    $(document).on "click", ".simple-ajax-btn", () ->
        url = $(this).data('url')
        method = $(this).data('method')
        if not method
            method = 'GET'
        onsuccess = $(this).data('onsuccess')
        $.ajax url,
            type: method
            dataType: 'html'
            success: (data, textStatus, jqXHR) ->
                if onsuccess == 'refresh'
                    location.reload(true)
                return false
        return false

    $(document).on "click", ".disabled", () ->
        return false

    # Switching checkbox with class 'chk-radiogroup' to ON will uncheck all other checkboxes of the same group
    window.chkradio_semafor = false
    $(document).on 'switchChange.bootstrapSwitch', ".chk-radiogroup", (event, state) ->
        if window.chkradio_semafor
            return true
        if not state
            return true
        window.chkradio_semafor = true
        radiogroup = $(this).data('radiogroup')
        name = $(this).attr('name')
        $(".#{radiogroup}").each ->
            thisname = $(this).attr('name')
            if thisname != name
                $(this).data("bootstrap-switch").state(false)
            true
        window.chkradio_semafor = false
        true

    setTimeout content_loaded, 1000

    window.mask_num = (selector) ->
        $(selector).unmask()
        $(selector).mask '#,##0',
            reverse: true,
            translation: {
                '#': {
                    pattern: /-|\d/,
                    recursive: true
                }
            },
            onChange: (value, e) ->
                target = e.target
                tag = $(target).prop("tagName")
                newvalue = value.replace(/(?!^)-/g, '').replace(/^,/, '').replace(/^-,/, '-')
                if tag == 'INPUT'
                    if $(target).is(':focus')
                        position = target.selectionStart  # Capture initial position
                        target.value = newvalue
                        target.selectionEnd = position  # Set the cursor back to the initial position.
                    else
                        target.value = newvalue
                else
                    target.innerHTML = newvalue
                true
        true
    # Masking
    $('input[type="tel"]').mask('000-000-0000')
    $('input.number-field.positive-number').mask('#,##0', {'reverse': true})
    mask_num('input.number-field.allow-negative')
    mask_num('span.number-field')
    $('input.year-field').mask('0000', {'reverse': true})
    $('input.float-field').mask('#,##0.00', {'reverse': true})
    $('input.zip-field').mask('000000')
    $('input.ssn-field').mask('000-00-0000')
    $('input.caf-field').mask('0000-00000')
    $('input.ptin-field').mask('00000000')
    $('input#id_routing_number').mask('0000000000')
    $('input#id_account_number').mask('00000000000000000')
    $('.justyears input').mask('0000')

    # $(document).on 'change', 'input.number-field', () ->
    #     # just to remove trailing zero
    #     $(this).val(myparseInt($(this).val())).keyup()
    #     return true

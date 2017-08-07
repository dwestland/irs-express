'use strict'
$ ->

    window.reload_ajax = (selector) ->
        url = $(selector).data('src')
        $.ajax url,
            type: 'GET'
            dataType: 'html'
            success: (data, textStatus, jqXHR) ->
                $(selector).html(data)
        return false

    window.client_update = (client_data, onsuccess) ->
        client_id = $('#object_data').data('objectid')
        url = $('.cp-content').data('src')
        csrftoken = Cookies.get('csrftoken')
        $.ajax url,
            type: 'PUT'
            dataType: 'json'
            contentType: "application/json"
            data: JSON.stringify(client_data)
            success: onsuccess
        return false

    $('.client-delete-btn').click ->
        if confirm("Are you sure you want to delete this item?\nThis operation cannot be undone!")
            url = $(this).data('url')
            success_url = $(this).data('success-url')
            $.ajax url,
                type: 'POST'
                success: (data, textStatus, jqXHR) ->
                    window.location.href = success_url
                    return false
        return false

    $('.client-status-btn').click ->
        element = this
        $('.client-status-btn').removeClass('active')
        $('.client-status-btn span.fa').removeClass('fa-check')
        newstatus = $(this).data('status')
        client_update {'status': newstatus}, (data, textStatus, jqXHR) ->
            reload_ajax('.cp-content')
            $(element).addClass('active')
            $('span.fa', element).addClass('fa-check')
        return false

    # BEGIN - "not saved" indicator code
    # If client summary changed - show "not saved" indicator
    window.client_summary_change = () ->
        if $('#client_summary').val() != $('#client_summary_saved').val()
            $('.summary-saved-indicator').hide()
            $('.summary-notsaved-indicator').show()
        else
            $('.summary-saved-indicator').show()
            $('.summary-notsaved-indicator').hide()

    $('#client_summary').change ->
        client_summary_change()
    $('#client_summary').keyup ->
        client_summary_change()

    $('.summary-save-btn').click ->
        summary_data = $("#client_summary").val()
        client_update {'summary': summary_data}, (data, textStatus, jqXHR) ->
            $('#client_summary_saved').val($('#client_summary').val())
            client_summary_change()
        return false

    $('.summary-notsaved-indicator').removeClass('hidden')
    $('.summary-notsaved-indicator').hide()
    $('.summary-saved-indicator').removeClass('hidden')

    # END - "not saved" indicator code

    # BEGIN - PDF edit code

    $('button.pdfedit-btn').click ->
        alert("Not implemented yet, sorry")
        return false

    # END - PDF edit code

    # BEGIN - note/doc add/edit/delete

    $(document).on "click", '.edit-notedoc-btn', () ->
        url = $(this).data('url')
        modalform = $(".modal-element")
        $.ajax url,
            type: 'GET'
            dataType: 'html'
            success: (data, textStatus, jqXHR) ->
                $(modalform).html(data)
                reinitWidgets()
                $('.modalform', modalform).modal('show')
                $('.formsavebtn', modalform).click ->
                    $('form', modalform).ajaxSubmit()
                    $('.modalform', modalform).modal('hide')
                    reload_ajax('.notes-list')
        return false

    $(document).on "click", '.delete-notedoc-btn', () ->
        url = $(this).data('url')
        can_delete = confirm("Are you sure you want to delete this element?")
        if not can_delete
            return false
        $.ajax url,
            type: 'DELETE'
            dataType: 'html'
            success: (data, textStatus, jqXHR) ->
                reload_ajax('.notes-list')
                return false
        return false

    # END - note/doc add/edit/delete

    # BEGIN - stage increase/decrease

    $(document).on "click", '.stagebtn', () ->
        newstage = $(this).data('newstage')
        client_update {'stage': newstage}, (data, textStatus, jqXHR) ->
            reload_ajax('.cp-content')
            reload_ajax('.notes-list')
            return false
        return false

    # END - stage increase/decrease

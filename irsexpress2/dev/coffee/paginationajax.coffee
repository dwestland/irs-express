'use strict'
$ ->
    # navigation
    curpage = 1
    sortfield = $('.pagination-sortfield').data('field')
    ascsort = $('.pagination-sortfield').data('asc')
    if "#{ascsort}" not in ['0', '1']
        ascsort = "1"
    disableEvents = false

    navigate = (page=null) ->
        page = page or curpage
        lfilters = ""
        for lfo in $('.input-filter')
            fname = $(lfo).attr('name')
            fvalue = $(lfo).val()
            if fvalue != '-'
                lfilters += "&filters[]=#{fname}*#{fvalue}"
        for lfo in $('.chk-filter')
            if $(lfo).is(":checked")
                fname = $(lfo).attr('name')
                fvalue = $(lfo).val()
                if fvalue != '-'
                    lfilters += "&filters[]=#{fname}*#{fvalue}"
        for lfo in $('.list-filter')
            fname = $(lfo).attr('name')
            fvalue = $(lfo).val()
            if fvalue != '-'
                lfilters += "&filters[]=#{fname}*#{fvalue}"
        extravars = ""
        for lfo in $('.pagination-parameter')
            fname = $(lfo).data('name')
            fvalue = $(lfo).data('value')
            if fvalue != '-'
                extravars += "&#{fname}=#{fvalue}"
            # console.log(fname, fvalue)
        $.ajax window.location.pathname + "?&page="+page+lfilters+"&sort=#{sortfield}&asc=#{ascsort}"+extravars,
            type: 'GET'
            dataType: 'html'
            success: (data, textStatus, jqXHR) ->
                curpage = page
                $('.paginated_content').html(data)
                reinitWidgets()
                # sorting styling
                hhh = $("[data-sort='#{sortfield}']").addClass('sortfield').html()
                if "#{ascsort}" == '1'
                    hhh = hhh.replace('</span></div>', ' <i class=" fa fa-sort-alpha-asc"></i></span></div>')
                    $("[data-sort='#{sortfield}']").addClass('sortasc').html(hhh)
                else
                    hhh = hhh.replace('</span></div>', ' <i class=" fa fa-sort-alpha-desc"></i></span></div>')
                    $("[data-sort='#{sortfield}']").addClass('sortdesc').html(hhh)
        return false

    window.navigate = navigate

    $(document).on 'click', '.listnav', () ->
        nextpage = $(this).data('page')
        if !nextpage
            return false
        navigate(nextpage)

    $(document).on 'change', '.list-filter', () ->
        if not disableEvents
            navigate(1)

    $(document).on 'click', '.chk-filter', () ->
        if not disableEvents
            navigate(1)
        return true

    $(document).on 'keyup', '.input-filter', () ->
        if not disableEvents
            navigate(1)

    $(document).on 'click', '.filter-reset', () ->
        disableEvents = true
        # $(".list-filter").select2('val', '-')
        for selobj in $(".input-filter")
            $(selobj).val('')
        for selobj in $(".list-filter")
            $(selobj).select2('val', '-')
        disableEvents = false
        navigate(1)

    $(document).on 'click', '[data-sort]', () ->
        mysortfield = $(this).data('sort')
        if sortfield == mysortfield
            ascsort = ascsort ^ 1
        else
            ascsort = 1
            sortfield = mysortfield
        navigate()
        
    if $('.paginated_content').length > 0
        navigate(1)

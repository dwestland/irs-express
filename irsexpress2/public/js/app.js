(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({"/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/app.js":[function(require,module,exports){
'use strict';
$(function() {
  var set_scrollable;
  window.pass = function() {
    return false;
  };
  window.myparseInt = function(value) {
    var val;
    val = parseInt(value.replace(/[\.,]/g, ''));
    return val;
  };
  window.waitload_list = {};
  window.content_loaded = function(name) {
    var all_loaded, item, notloaded;
    if (name) {
      console.log(name + " loaded");
      waitload_list[name] = false;
    }
    all_loaded = true;
    for (item in waitload_list) {
      notloaded = waitload_list[item];
      if (notloaded) {
        console.log("waiting for " + item + " to be loaded");
        all_loaded = false;
        break;
      }
    }
    if (all_loaded) {
      $('.content-load-wait').each(function() {
        var celem;
        celem = $(this).data('content-element');
        if (celem) {
          $(celem).removeClass('hidden');
        }
        reinitWidgets();
        return $(this).hide();
      });
    }
    return false;
  };
  window.waitvalidation_list = {};
  window.validating_form = "";
  window.form_validated = function(name, result) {
    var all_validated, item, validation_state;
    if (name) {
      console.log("form " + name + " validated (" + result + ")");
      waitvalidation_list[name] = result;
    }
    all_validated = true;
    for (item in waitvalidation_list) {
      validation_state = waitvalidation_list[item];
      if (validation_state === 1) {
        console.log("waiting for " + item + " to be validated");
        all_validated = false;
        break;
      }
      if (validation_state === 2) {
        console.log("form " + item + " validation failed");
        all_validated = false;
        $('.form-validation-wait').hide();
        break;
      }
    }
    if (all_validated && window.validating_form.length > 0) {
      console.log("submitting form");
      $(window.validating_form).submit();
      return true;
    }
  };
  window.reinitWidgets = function() {
    $('.toggle-chkbox').bootstrapSwitch();
    $('.switch-radio2').bootstrapSwitch();
    $('select').select2();
    $('.xtooltip').tooltip();
    return $('[data-toggle="popover"]').popover();
  };
  $('.img-popover').popover({
    trigger: 'hover',
    placement: 'right',
    content: function() {
      return '<img src="' + $(this).data('src') + '">';
    },
    title: "",
    html: true
  });
  reinitWidgets();
  $('.form-group').each(function() {
    var error_messages;
    error_messages = $(this).attr('error_messages');
    if (error_messages) {
      $(this).addClass('has-error');
      $('input', this).popover({
        placement: 'right',
        content: function() {
          return '<span class="text-danger">' + error_messages + '</span>';
        },
        title: "",
        html: true
      });
      return $('input', this).popover('show');
    }
  });
  set_scrollable = function() {
    var content_height, window_height;
    window_height = $(document).height();
    content_height = window_height - 300;
    return $('.scrollable').height(content_height);
  };
  $(window).resize(set_scrollable);
  set_scrollable();
  $(document).on("click", ".simple-ajax-btn", function() {
    var method, onsuccess, url;
    url = $(this).data('url');
    method = $(this).data('method');
    if (!method) {
      method = 'GET';
    }
    onsuccess = $(this).data('onsuccess');
    $.ajax(url, {
      type: method,
      dataType: 'html',
      success: function(data, textStatus, jqXHR) {
        if (onsuccess === 'refresh') {
          location.reload(true);
        }
        return false;
      }
    });
    return false;
  });
  $(document).on("click", ".disabled", function() {
    return false;
  });
  window.chkradio_semafor = false;
  $(document).on('switchChange.bootstrapSwitch', ".chk-radiogroup", function(event, state) {
    var name, radiogroup;
    if (window.chkradio_semafor) {
      return true;
    }
    if (!state) {
      return true;
    }
    window.chkradio_semafor = true;
    radiogroup = $(this).data('radiogroup');
    name = $(this).attr('name');
    $("." + radiogroup).each(function() {
      var thisname;
      thisname = $(this).attr('name');
      if (thisname !== name) {
        $(this).data("bootstrap-switch").state(false);
      }
      return true;
    });
    window.chkradio_semafor = false;
    return true;
  });
  setTimeout(content_loaded, 1000);
  window.mask_num = function(selector) {
    $(selector).unmask();
    $(selector).mask('#,##0', {
      reverse: true,
      translation: {
        '#': {
          pattern: /-|\d/,
          recursive: true
        }
      },
      onChange: function(value, e) {
        var newvalue, position, tag, target;
        target = e.target;
        tag = $(target).prop("tagName");
        newvalue = value.replace(/(?!^)-/g, '').replace(/^,/, '').replace(/^-,/, '-');
        if (tag === 'INPUT') {
          if ($(target).is(':focus')) {
            position = target.selectionStart;
            target.value = newvalue;
            target.selectionEnd = position;
          } else {
            target.value = newvalue;
          }
        } else {
          target.innerHTML = newvalue;
        }
        return true;
      }
    });
    return true;
  };
  $('input[type="tel"]').mask('000-000-0000');
  $('input.number-field.positive-number').mask('#,##0', {
    'reverse': true
  });
  mask_num('input.number-field.allow-negative');
  mask_num('span.number-field');
  $('input.year-field').mask('0000', {
    'reverse': true
  });
  $('input.float-field').mask('#,##0.00', {
    'reverse': true
  });
  $('input.zip-field').mask('000000');
  $('input.ssn-field').mask('000-00-0000');
  $('input.caf-field').mask('0000-00000');
  $('input.ptin-field').mask('00000000');
  $('input#id_routing_number').mask('0000000000');
  $('input#id_account_number').mask('00000000000000000');
  return $('.justyears input').mask('0000');
});

},{}],"/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/app_setup.js":[function(require,module,exports){
'use strict';
$(function() {
  var csrfSafeMethod, csrftoken;
  csrftoken = Cookies.get('csrftoken');
  csrfSafeMethod = function(method) {
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
  };
  return $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        return xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });
});

},{}],"/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/client_cp.js":[function(require,module,exports){
'use strict';
$(function() {
  window.reload_ajax = function(selector) {
    var url;
    url = $(selector).data('src');
    $.ajax(url, {
      type: 'GET',
      dataType: 'html',
      success: function(data, textStatus, jqXHR) {
        return $(selector).html(data);
      }
    });
    return false;
  };
  window.client_update = function(client_data, onsuccess) {
    var client_id, csrftoken, url;
    client_id = $('#object_data').data('objectid');
    url = $('.cp-content').data('src');
    csrftoken = Cookies.get('csrftoken');
    $.ajax(url, {
      type: 'PUT',
      dataType: 'json',
      contentType: "application/json",
      data: JSON.stringify(client_data),
      success: onsuccess
    });
    return false;
  };
  $('.client-delete-btn').click(function() {
    var success_url, url;
    if (confirm("Are you sure you want to delete this item?\nThis operation cannot be undone!")) {
      url = $(this).data('url');
      success_url = $(this).data('success-url');
      $.ajax(url, {
        type: 'POST',
        success: function(data, textStatus, jqXHR) {
          window.location.href = success_url;
          return false;
        }
      });
    }
    return false;
  });
  $('.client-status-btn').click(function() {
    var element, newstatus;
    element = this;
    $('.client-status-btn').removeClass('active');
    $('.client-status-btn span.fa').removeClass('fa-check');
    newstatus = $(this).data('status');
    client_update({
      'status': newstatus
    }, function(data, textStatus, jqXHR) {
      reload_ajax('.cp-content');
      $(element).addClass('active');
      return $('span.fa', element).addClass('fa-check');
    });
    return false;
  });
  window.client_summary_change = function() {
    if ($('#client_summary').val() !== $('#client_summary_saved').val()) {
      $('.summary-saved-indicator').hide();
      return $('.summary-notsaved-indicator').show();
    } else {
      $('.summary-saved-indicator').show();
      return $('.summary-notsaved-indicator').hide();
    }
  };
  $('#client_summary').change(function() {
    return client_summary_change();
  });
  $('#client_summary').keyup(function() {
    return client_summary_change();
  });
  $('.summary-save-btn').click(function() {
    var summary_data;
    summary_data = $("#client_summary").val();
    client_update({
      'summary': summary_data
    }, function(data, textStatus, jqXHR) {
      $('#client_summary_saved').val($('#client_summary').val());
      return client_summary_change();
    });
    return false;
  });
  $('.summary-notsaved-indicator').removeClass('hidden');
  $('.summary-notsaved-indicator').hide();
  $('.summary-saved-indicator').removeClass('hidden');
  $('button.pdfedit-btn').click(function() {
    alert("Not implemented yet, sorry");
    return false;
  });
  $(document).on("click", '.edit-notedoc-btn', function() {
    var modalform, url;
    url = $(this).data('url');
    modalform = $(".modal-element");
    $.ajax(url, {
      type: 'GET',
      dataType: 'html',
      success: function(data, textStatus, jqXHR) {
        $(modalform).html(data);
        reinitWidgets();
        $('.modalform', modalform).modal('show');
        return $('.formsavebtn', modalform).click(function() {
          $('form', modalform).ajaxSubmit();
          $('.modalform', modalform).modal('hide');
          return reload_ajax('.notes-list');
        });
      }
    });
    return false;
  });
  $(document).on("click", '.delete-notedoc-btn', function() {
    var can_delete, url;
    url = $(this).data('url');
    can_delete = confirm("Are you sure you want to delete this element?");
    if (!can_delete) {
      return false;
    }
    $.ajax(url, {
      type: 'DELETE',
      dataType: 'html',
      success: function(data, textStatus, jqXHR) {
        reload_ajax('.notes-list');
        return false;
      }
    });
    return false;
  });
  return $(document).on("click", '.stagebtn', function() {
    var newstage;
    newstage = $(this).data('newstage');
    client_update({
      'stage': newstage
    }, function(data, textStatus, jqXHR) {
      reload_ajax('.cp-content');
      reload_ajax('.notes-list');
      return false;
    });
    return false;
  });
});

},{}],"/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/irs433a.js":[function(require,module,exports){
'use strict';
$(function() {
  var data, element, form433a_page, i, len, sugg, suggestions;
  form433a_page = $('.433A-pageactive').data('value');
  if (form433a_page === 'is_page4_active') {
    $(document).on("keyup", ".form433a .account_balance", function() {
      var sum;
      sum = 0;
      $(".form433a .account_balance").each(function() {
        sum += myparseInt($(this).val());
        return true;
      });
      return $(".form433a #id_total_cash").val(sum).keyup();
    });
    $(document).on("keyup", ".form433a .loan_balance_curval", function() {
      var cv, equity, lb;
      lb = cv = 0;
      $(".form433a .loan_balance").each(function() {
        lb += myparseInt($(this).val());
        return true;
      });
      $(".form433a .current_value").each(function() {
        cv += myparseInt($(this).val());
        return true;
      });
      equity = cv - lb;
      return $(".form433a #id_total_equity").val(equity).keyup();
    });
    $(document).on("keyup", ".form433a .amount_owed_crlimit", function() {
      var ao, cl, total_credit;
      ao = cl = 0;
      $(".form433a .amount_owed").each(function() {
        ao += myparseInt($(this).val());
        return true;
      });
      $(".form433a .credit_limit").each(function() {
        cl += myparseInt($(this).val());
        return true;
      });
      total_credit = cl - ao;
      return $(".form433a #id_total_credit").val(total_credit).keyup();
    });
    $(document).on("keyup", ".form433a .cash_value_lbal", function() {
      var acash, cv, lb;
      lb = cv = 0;
      $(".form433a .iiloan_balance").each(function() {
        lb += myparseInt($(this).val());
        return true;
      });
      $(".form433a .cash_value").each(function() {
        cv += myparseInt($(this).val());
        return true;
      });
      acash = cv - lb;
      return $(".form433a #id_total_available_cash").val(acash).keyup();
    });
  }
  if (form433a_page === 'is_page5_active') {
    $(document).on("keyup", ".form433a .rpfmv_clb", function() {
      var equity, lb, mv;
      lb = mv = 0;
      $(".form433a .rpcurrent_loan_balance").each(function() {
        lb += myparseInt($(this).val());
        return true;
      });
      $(".form433a .rpmarket_value").each(function() {
        mv += myparseInt($(this).val());
        return true;
      });
      equity = mv - lb;
      return $(".form433a #id_real_property_total_equity").val(equity).keyup();
    });
    $(document).on("keyup", ".form433a .vvfmv_clb", function() {
      var equity, lb, mv;
      lb = mv = 0;
      $(".form433a .vvcurrent_loan_balance").each(function() {
        lb += myparseInt($(this).val());
        return true;
      });
      $(".form433a .vvmarket_value").each(function() {
        mv += myparseInt($(this).val());
        return true;
      });
      equity = mv - lb;
      return $(".form433a #id_vehicles_total_equity").val(equity).keyup();
    });
    $(document).on("keyup", ".form433a .pafmv_clb", function() {
      var equity, lb, mv;
      lb = mv = 0;
      $(".form433a .pacurrent_loan_balance").each(function() {
        lb += myparseInt($(this).val());
        return true;
      });
      $(".form433a .pamarket_value").each(function() {
        mv += myparseInt($(this).val());
        return true;
      });
      equity = mv - lb;
      return $(".form433a #id_personal_assets_total_equity").val(equity).keyup();
    });
    $(document).on("click", ".form433a .pa-sethomeaddress", function() {
      var elem, fk, hldata, this_tr, value;
      this_tr = $(this).closest('tr');
      hldata = $('.formelement-home_location input', this_tr).val();
      hldata = JSON.parse(hldata);
      for (fk in hldata) {
        value = hldata[fk];
        if (fk === 'location_county' || fk === 'location_state_name') {
          elem = $(".formelement-" + fk + " select", this_tr);
        } else {
          elem = $(".formelement-" + fk + " input", this_tr);
        }
        if (elem.length > 0) {
          $(elem).val(value).trigger('change');
        }
      }
      return false;
    });
  }
  if (form433a_page === 'is_page6_active') {
    suggestions = $('.irs-suggestions-data').html();
    suggestions = JSON.parse(suggestions);
    for (i = 0, len = suggestions.length; i < len; i++) {
      sugg = suggestions[i];
      element = $(sugg['element-selector']);
      data = '<p class="sugg"><span class="' + sugg['class'] + '">IRS Express suggests: <span class="value">' + sugg['value'] + '</span></span><span class="desc">' + sugg['desc'] + '</span></p>';
      $(data).insertAfter(element);
    }
    window.calc_expenses = function() {
      var expense, income, netdiff;
      income = expense = 0;
      $(".form433a .income_field").each(function() {
        var hval;
        if ($(this).attr('id') === 'id_net_business_income') {
          hval = $(this).html().replace(/[\<\>span\s\$\/]/g, '');
          income += myparseInt(hval);
        } else {
          income += myparseInt($(this).val());
        }
        return true;
      });
      $(".form433a .expense_field").each(function() {
        expense += myparseInt($(this).val());
        return true;
      });
      $(".form433a #id_total_income_cnt span").html(income).keyup();
      $(".form433a #id_total_expenses_cnt span").html(expense).keyup();
      netdiff = income - expense;
      return $(".form433a #id_net_difference_cnt span").html(netdiff).keyup();
    };
    $(document).on("keyup", ".form433a .inpfld", function() {
      return calc_expenses();
    });
    calc_expenses();
    mask_num(".form433a #id_net_business_income span");
    mask_num(".form433a #id_total_income_cnt span");
    mask_num(".form433a #id_total_expenses_cnt span");
    mask_num(".form433a #id_net_difference_cnt span");
  }
  if (form433a_page === 'is_page7_active') {
    window.hide_page7_elements = function() {
      return $('.form433a-page-7 > table > tbody > tr').each(function() {
        var this_tr;
        this_tr = $(this);
        if ($('input[name="is_self_employed"]', this_tr).length > 0) {
          return true;
        }
        this_tr.hide();
        return true;
      });
    };
    window.show_page7_elements = function() {
      $('.form433a-page-7 > table > tbody > tr').each(function() {
        var this_tr;
        this_tr = $(this);
        if ($('input[name="is_self_employed"]', this_tr).length > 0) {
          return true;
        }
        this_tr.show();
        return true;
      });
      if (!$('.form433a input[name="has_bank_account"]').data("bootstrap-switch").state()) {
        $('.showhidewith-chk-businessbankacc').closest('tr.fieldrow').hide();
      }
      if (!$('.form433a input[name="has_accounts_receivable"]').data("bootstrap-switch").state()) {
        $('.showhidewith-chk-accountsreceivable').closest('tr.fieldrow').hide();
      }
      if (!$('.form433a input[name="has_business_assets"]').data("bootstrap-switch").state()) {
        return $('.showhidewith-chk-businessasset').closest('tr.fieldrow').hide();
      }
    };
    $('.form433a input[name="is_self_employed"]').on('switchChange.bootstrapSwitch', function(event, state) {
      var this_tr;
      if (state) {
        this_tr = $(this).closest('tr');
        show_page7_elements();
      } else {
        hide_page7_elements();
      }
      return true;
    });
    if (!$('.form433a input[name="is_self_employed"]').data("bootstrap-switch").state()) {
      hide_page7_elements();
    }
    $(document).on("keyup", ".form433a .bba_account_balance", function() {
      var cbnk;
      cbnk = 0;
      $(".form433a .bba_account_balance").each(function() {
        cbnk += myparseInt($(this).val());
        return true;
      });
      return $(".form433a #id_total_cash_in_banks").val(cbnk).keyup();
    });
    $(document).on("keyup", ".form433a .ar_amount_due", function() {
      var arad;
      arad = 0;
      $(".form433a .ar_amount_due").each(function() {
        arad += myparseInt($(this).val());
        return true;
      });
      return $(".form433a #id_outstanding_balance").val(arad).keyup();
    });
    $(document).on("keyup", ".form433a .bafmv_clb", function() {
      var equity, lb, mv;
      lb = mv = 0;
      $(".form433a .bacurrent_loan_balance").each(function() {
        lb += myparseInt($(this).val());
        return true;
      });
      $(".form433a .bamarket_value").each(function() {
        mv += myparseInt($(this).val());
        return true;
      });
      equity = mv - lb;
      return $(".form433a #id_total_equity").val(equity).keyup();
    });
    $(document).on("click", ".form433a .pa-setbusinessaddress", function() {
      var bselem, elem, j, len1, lname, locnames, this_tr;
      this_tr = $(this).closest('tr');
      locnames = ['street', 'city', 'state_name', 'zipcode', 'county'];
      for (j = 0, len1 = locnames.length; j < len1; j++) {
        lname = locnames[j];
        if (lname === 'county' || lname === 'state_name') {
          elem = $(".formelement-location_" + lname + " select", this_tr);
        } else {
          elem = $(".formelement-location_" + lname + " input", this_tr);
        }
        bselem = $("#id_business_" + lname);
        if (elem.length > 0 && bselem.length > 0) {
          console.log("Set " + lname);
          $(elem).val($(bselem).val()).trigger('change');
        } else {
          console.log("Cannot set " + lname);
        }
      }
      return false;
    });
  }
  if (form433a_page === 'is_page8_active') {
    window.calc_expenses = function() {
      var expense, income, netdiff;
      income = expense = 0;
      $(".form433a .income_field").each(function() {
        income += myparseInt($(this).val());
        return true;
      });
      $(".form433a .expense_field").each(function() {
        expense += myparseInt($(this).val());
        return true;
      });
      $(".form433a #id_total_income_cnt span").html(income).keyup();
      $(".form433a #id_total_expenses_cnt span").html(expense).keyup();
      netdiff = income - expense;
      return $(".form433a #id_net_difference_cnt span").html(netdiff).keyup();
    };
    $(document).on("keyup", ".form433a .inpfld", function() {
      return calc_expenses();
    });
    mask_num(".form433a #id_total_income_cnt span");
    mask_num(".form433a #id_total_expenses_cnt span");
    mask_num(".form433a #id_net_difference_cnt span");
    return calc_expenses();
  }
});

},{}],"/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/irs656.js":[function(require,module,exports){
'use strict';
$(function() {
  var form656_page, i, initial_payment, j, monthNames, offer_amount, payment_val;
  form656_page = $('.656-pageactive').data('value');
  monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  if (form656_page === 'is_page5_active') {
    window.f656page5_recalc_lumpsum = function() {
      var adday, admonth, adyear, can_pay, cnt, debt, expdate, i, income, initial_payment, j, months, nowtime, offer_amount, payment_1, payment_2, payment_3, payment_4, payment_5, rem, remaining_balance, results, value;
      admonth = myparseInt($('#id_assessed_date_month').val()) - 1;
      adday = myparseInt($('#id_assessed_date_day').val());
      adyear = myparseInt($('#id_assessed_date_year').val());
      if (admonth === 0 || adday === 0 || adyear === 0) {
        $('#id_statute_exp_date').html('-');
        $('#id_statute_months_avail').html('-');
        $('#lumpsum_decision').html('probably may be');
        $('#id_suggested_amount span').html('0').keyup();
        return $('#id_can_pay span').html("0").keyup();
      } else {
        expdate = new Date(adyear + 10, admonth, adday);
        nowtime = new Date();
        months = ((expdate - nowtime) / (1000 * 60 * 60 * 24 * 30.44)).toFixed();
        $('#id_statute_exp_date').html(monthNames[admonth] + "/" + adday + "/" + (adyear + 10));
        $('#id_statute_months_avail').html(months + " months");
        income = myparseInt($('#id_monthly_income').val());
        debt = myparseInt($('#id_debt_total').val());
        can_pay = months * income;
        $('#id_can_pay span').html("" + can_pay).keyup();
        if (can_pay < debt) {
          $('#lumpsum_decision').html('MAY be');
        } else {
          $('#lumpsum_decision').html('NOT');
        }
        $('#id_suggested_amount span').html("" + (income * 12)).keyup();
        offer_amount = myparseInt($('#id_offer_amount_lumpsum').val());
        initial_payment = myparseInt($('#id_initial_payment').val());
        payment_1 = myparseInt($('#id_payment_1').val());
        payment_2 = myparseInt($('#id_payment_2').val());
        payment_3 = myparseInt($('#id_payment_3').val());
        payment_4 = myparseInt($('#id_payment_4').val());
        payment_5 = myparseInt($('#id_payment_5').val());
        if (offer_amount === 0 || !window.offer_amount_changed) {
          offer_amount = income * 12;
          $('#id_offer_amount_lumpsum').val(offer_amount).keyup();
          mark_unsaved();
        }
        if (initial_payment === 0 || !window.initial_payment_changed) {
          initial_payment = (offer_amount / 5).toFixed();
          $('#id_initial_payment').val(initial_payment).keyup();
          mark_unsaved();
        }
        remaining_balance = offer_amount - initial_payment;
        $('#id_remaining_balance span').html(remaining_balance).keyup();
        rem = remaining_balance;
        cnt = 6;
        results = [];
        for (i = j = 1; j <= 5; i = ++j) {
          value = (rem / (cnt - i)).toFixed();
          rem = rem - value;
          $("#payment_" + i + "_advice span.field-number").html(value).keyup();
          if (!window.payments_changed[i]) {
            results.push($("#id_payment_" + i).val(value).keyup());
          } else {
            results.push(void 0);
          }
        }
        return results;
      }
    };
    offer_amount = myparseInt($('#id_offer_amount_lumpsum').val());
    initial_payment = myparseInt($('#id_initial_payment').val());
    window.offer_amount_changed = offer_amount > 0;
    window.initial_payment_changed = initial_payment > 0;
    window.payments_changed = [false, false, false, false, false];
    for (i = j = 1; j <= 5; i = ++j) {
      payment_val = myparseInt($("#id_payment_" + i).val());
      window.payments_changed[i] = payment_val > 0;
      $("#id_payment_" + i).css('width', 200).css('display', 'inline');
      $('<span id="payment_' + i + '_advice" data-pi="' + i + '" class="payment_advice"><span class="fa fa-arrow-left"></span> $ <span class="field-number">0</span></span>').insertAfter("#id_payment_" + i);
    }
    $(document).on('click', '.payment_advice', function() {
      var pi, thistr, v;
      v = $('span.field-number', this).html();
      thistr = $(this).closest('tr');
      $('input', thistr).val(v).keyup();
      pi = $(this).data('pi');
      return window.payments_changed[pi] = false;
    });
    f656page5_recalc_lumpsum();
    $('.formelement-assessed_date').on('change', 'select', function() {
      return f656page5_recalc_lumpsum();
    });
    $('#id_monthly_income').on('change', function() {
      return f656page5_recalc_lumpsum();
    });
    $('#id_debt_total').on('change', function() {
      return f656page5_recalc_lumpsum();
    });
    $('#id_offer_amount_lumpsum').on('change', function() {
      window.offer_amount_changed = true;
      return f656page5_recalc_lumpsum();
    });
    return $('#id_initial_payment').on('change', function() {
      window.initial_payment_changed = true;
      return f656page5_recalc_lumpsum();
    });
  }
});

},{}],"/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/irs_common.js":[function(require,module,exports){
'use strict';
$(function() {
  var formid;
  if ($('form#pageform .irsform').length > 0) {
    window.disable_switch = false;
    window.show_1x1_subform = function(prev, src_url, unlock_name) {
      if (!src_url) {
        console.exception("1x1 subform: src_url is empty!");
        return false;
      }
      return $.ajax(src_url, {
        type: 'GET',
        dataType: 'html',
        success: function(data, textStatus, jqXHR) {
          $(data).insertAfter(prev);
          reinitWidgets();
          if (unlock_name) {
            content_loaded(unlock_name);
          }
          return false;
        }
      });
    };
    $('.irsform input.form1x1switcher').on('switchChange.bootstrapSwitch', function(event, state) {
      var src_url, subform_selector, subformname, this_tr;
      if (window.disable_switch) {
        return true;
      }
      window.disable_switch = true;
      subformname = $(this).data('subform-name');
      src_url = $("#" + subformname + "_form_url").data('url');
      subform_selector = $("#" + subformname + "_form_url").data('subform-selector');
      if (state) {
        this_tr = $(this).closest('tr');
        show_1x1_subform(this_tr, src_url);
      } else {
        if (!confirm("This action will remove the section below. Are you sure?")) {
          window.disable_switch = true;
          $(this).data("bootstrap-switch").state(true);
          window.disable_switch = false;
          return true;
        }
        $(this).data("bootstrap-switch").state(false);
        $(subform_selector).remove();
      }
      window.disable_switch = false;
      return true;
    });
    if ($('.irsform input.form1x1switcher').length > 0) {
      $('.irsform input.form1x1switcher').each(function() {
        var src_url, subformname, this_tr;
        subformname = $(this).data('subform-name');
        src_url = $("#" + subformname + "_form_url").data('url');
        if ($(this).data("bootstrap-switch").state()) {
          waitload_list[subformname] = true;
          this_tr = $(this).closest('tr');
          show_1x1_subform(this_tr, src_url, subformname);
        }
        return true;
      });
    }
    window.adjust_calculations = function() {
      $('.form433a-page-4 input.number-field').keyup();
      $('.form433a-page-5 input.number-field').keyup();
      return $('.form433a-page-7 input.number-field').keyup();
    };
    window.subforms_1xn_counts = {};
    window.subforms_1xn_maxcounts = {};
    window.add_1xn_subform = function(prev, src_url, subformname, unlock_name) {
      var cnt, maxcnt;
      if (!src_url) {
        console.exception("1xn subform: src_url is empty!");
        return false;
      }
      maxcnt = window.subforms_1xn_maxcounts[subformname];
      cnt = window.subforms_1xn_counts[subformname];
      if (maxcnt > 0 && cnt === maxcnt) {
        alert("Allowed only " + maxcnt + " items");
        return false;
      }
      src_url = $("#" + subformname + "_form_url").data('url');
      window.subforms_1xn_counts[subformname] += 1;
      cnt = window.subforms_1xn_counts[subformname];
      $.ajax("" + src_url + subformname + "_" + cnt, {
        type: 'GET',
        dataType: 'html',
        success: function(data, textStatus, jqXHR) {
          $(data).insertAfter(prev);
          reinitWidgets();
          adjust_calculations();
          if (unlock_name) {
            return content_loaded(unlock_name);
          }
        }
      });
      return false;
    };
    window.toggle1xNformset = function(element, managed) {
      var dsse, selector, src_url, state, subformname, this_tr;
      subformname = $(element).data('subform-name');
      state = $(element).data("bootstrap-switch").state();
      if (state) {
        this_tr = $(element).closest('tr');
        window.subforms_1xn_counts[subformname] = 0;
        src_url = $("#" + subformname + "_form_url").data('url');
        add_1xn_subform(this_tr, src_url, subformname);
        $('.showhidewith-chk-' + subformname).closest('tr.fieldrow').show();
      } else {
        if (managed) {
          if (!confirm("This action will remove the section below. Are you sure?")) {
            window.disable_switch = true;
            $(element).data("bootstrap-switch").state(true);
            window.disable_switch = false;
            return false;
          }
        }
        dsse = window.disable_switch;
        window.disable_switch = true;
        $(element).data("bootstrap-switch").state(false);
        window.disable_switch = dsse;
        selector = $("#" + subformname + "_form_url").data('subform-selector');
        $(selector).remove();
        window.subforms_1xn_counts[subformname] = 0;
        $('.showhidewith-chk-' + subformname).closest('tr.fieldrow').hide();
      }
      return true;
    };
    $('.irsform input.form1xnswitcher').on('switchChange.bootstrapSwitch', function(event, state) {
      if (window.disable_switch) {
        return true;
      }
      window.disable_switch = true;
      toggle1xNformset($(this), true);
      window.disable_switch = false;
      return true;
    });
    $('form#pageform').on("click", ".add-subform", function() {
      var src_url, subformclassname, subformname, this_tr;
      this_tr = $(this).closest('tr');
      subformclassname = $(this_tr).data('subform-classname');
      subformname = $('*[data-subform-selector=".' + subformclassname + '"]').data('subform-name');
      src_url = $("#" + subformname + "_form_url").data('url');
      add_1xn_subform(this_tr, src_url, subformname);
      return false;
    });
    $('form#pageform').on("click", ".remove-subform", function() {
      var subformclassname, subformname, switcher, this_tr;
      this_tr = $(this).closest('tr');
      subformclassname = $(this_tr).data('subform-classname');
      subformname = $('*[data-subform-selector=".' + subformclassname + '"]').data('subform-name');
      $(this_tr).remove();
      adjust_calculations();
      if ($("." + subformclassname).length === 0) {
        window.disable_switch = true;
        switcher = $(".irsform input.form1xnswitcher.switcher-" + subformname);
        switcher.data("bootstrap-switch").state(false);
        toggle1xNformset(switcher, false);
        window.disable_switch = false;
        $('.showhidewith-chk-' + subformname).closest('tr.fieldrow').hide();
      }
      return false;
    });
    if ($('.irsform input.form1xnswitcher').length > 0) {
      $('.irsform input.form1xnswitcher').each(function() {
        var i, ref, src_url, subform_cnt, subform_maxcnt, subformname, this_tr, x;
        subformname = $(this).data('subform-name');
        subform_cnt = $(this).data('subform-count');
        subform_maxcnt = $(this).data('subform-maxcount');
        window.subforms_1xn_counts[subformname] = 0;
        window.subforms_1xn_maxcounts[subformname] = subform_maxcnt;
        if (subform_cnt > 0) {
          src_url = $("#" + subformname + "_form_url").data('url');
          this_tr = $(this).closest('tr');
          $(this).data("bootstrap-switch").state(true);
          for (x = i = 1, ref = subform_cnt; 1 <= ref ? i < ref : i > ref; x = 1 <= ref ? ++i : --i) {
            waitload_list[subformname + "_" + x] = true;
            add_1xn_subform(this_tr, src_url, subformname, subformname + "_" + x);
          }
          $('.showhidewith-chk-' + subformname).closest('tr.fieldrow').show();
        } else {
          $('.showhidewith-chk-' + subformname).closest('tr.fieldrow').hide();
        }
        return true;
      });
    }
    $(document).on('switchChange.bootstrapSwitch', '.chk-radiogroup', function(event, state) {
      var deptr, deptrs, i, len, results, trelem;
      deptrs = $(this).data('dep_rows').split(' ');
      results = [];
      for (i = 0, len = deptrs.length; i < len; i++) {
        deptr = deptrs[i];
        trelem = $(".formelement-" + deptr).closest('tr');
        if (state) {
          trelem.removeClass('hidden');
          results.push($("#id_" + deptr).removeClass('hidden'));
        } else {
          if (!trelem.hasClass('hidden')) {
            results.push(trelem.addClass('hidden'));
          } else {
            results.push(void 0);
          }
        }
      }
      return results;
    });
    if ($('.toggle-chkbox.disabled').length > 0) {
      $('.toggle-chkbox.disabled').data("bootstrap-switch").disabled(true);
    }
    window.mark_unsaved = function(element) {
      if (window.form_saved) {
        window.form_saved = false;
        $('.form_save_page').removeClass('hidden');
        return $('div#formaffix').removeClass('hidden');
      }
    };
    window.mark_saved = function() {
      if (!window.form_saved) {
        window.form_saved = true;
        $('.form_save_page').addClass('hidden');
        return $('div#formaffix').addClass('hidden');
      }
    };
    formid = $('input[name="id"]').val();
    if (formid) {
      window.form_saved = false;
      mark_saved();
    } else {
      window.form_saved = true;
      mark_unsaved();
    }
    $('form#pageform').on('change', '.irsform input, .irsform select, .irsform textarea', function() {
      var elem;
      elem = $(this);
      mark_unsaved(elem);
      return true;
    });
    $('form#pageform').on('switchChange.bootstrapSwitch', '.irsform input.toggle-chkbox', function(event, state) {
      var elem;
      elem = $(this);
      mark_unsaved(elem);
      return true;
    });
    window.submit_irs_form = function(next_page, save) {
      var all_inputs, all_selects, all_textareas, ecount, form_data, form_name, form_selector, process_elements, src_url, v;
      window.validating_form = "";
      form_selector = "#pageform";
      form_data = {};
      form_data['do_form_save'] = save;
      form_name = 'mainform';
      ecount = 0;
      process_elements = function(elements) {
        return elements.each(function() {
          var name, type, value;
          name = $(this).attr('name');
          type = $(this).attr('type');
          value = $(this).val();
          if (type === 'checkbox') {
            value = $(this).data("bootstrap-switch").state();
          }
          form_data[name] = value;
          return true;
        });
      };
      all_inputs = $(form_selector + " input");
      all_selects = $(form_selector + " select");
      all_textareas = $(form_selector + " textarea");
      v = process_elements(all_inputs);
      v = process_elements(all_selects);
      v = process_elements(all_textareas);
      if ((typeof form443a_page !== "undefined" && form443a_page !== null) && form443a_page === 'is_page6_active') {
        form_data['net_business_income'] = 0;
      }
      src_url = $(window.validating_form).attr('action');
      $.ajax(src_url, {
        type: 'POST',
        dataType: 'html',
        data: $.param(form_data),
        success: function(data, textStatus, jqXHR) {
          var errorlist, errors, errortxt, etxt, fieldname, i, j, jsdata, len, len1;
          $('ul.errorlist').remove();
          if (data !== 'OK') {
            jsdata = JSON.parse(data);
            for (i = 0, len = jsdata.length; i < len; i++) {
              errors = jsdata[i];
              fieldname = errors[0];
              errorlist = errors[1];
              errortxt = '<ul class="errorlist">';
              for (j = 0, len1 = errorlist.length; j < len1; j++) {
                etxt = errorlist[j];
                errortxt += "<li>" + etxt + "</li>";
              }
              errortxt += '</ul>';
              $(errortxt).insertAfter('label[for*="id_' + fieldname + '"]');
            }
            form_validated(form_name, 2);
            alert("Some fields are filled incorrectly.\nPlease fix issues and submit the form again.");
          } else {
            form_validated(form_name, 0);
            if (save) {
              mark_saved();
              if ($('.form-id[value=""]').length > 0 && !next_page) {
                next_page = window.location.href;
              }
            }
            if (next_page) {
              window.location.href = next_page;
              return false;
            }
            return true;
          }
          return false;
        }
      });
      return false;
    };
    $(document).on("click", ".irsform-form-save", function() {
      var next_page;
      next_page = $(this).data('url');
      submit_irs_form(next_page, true);
      return false;
    });
    return window.onbeforeunload = function() {
      if (window.form_saved) {
        return void 0;
      }
      submit_irs_form(null, false);
      return ' ';
    };
  }
});

},{}],"/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/navigation.js":[function(require,module,exports){
'use strict';
$(function() {});

},{}],"/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/oic_calc.js":[function(require,module,exports){
'use strict';
$(function() {
  var monthNames;
  monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  $('#oic_calc_btn').click(function() {
    var client_id, elemid, modalform, url;
    elemid = $(this).data('id');
    url = $(this).data('sourceurl');
    if ($('#object_data.client-id').length > 0) {
      client_id = $('#object_data.client-id').data('objectid');
      url = "" + url + client_id;
    }
    modalform = $(".modal-element");
    $.ajax(url, {
      type: 'GET',
      dataType: 'html',
      success: function(data, textStatus, jqXHR) {
        $(modalform).html(data);
        reinitWidgets();
        $('.modalform', modalform).modal({
          show: true
        }, {
          keyboard: true
        });
        $('.modal .formsavebtn', modalform).click(function() {
          $('form', modalform).ajaxSubmit();
          return $('.modalform', modalform).modal('hide');
        });
        oic_calculator();
        return false;
      }
    });
    return false;
  });
  window.oic_calculator = function() {
    var adday, admonth, adyear, can_pay, debt, expdate, income, months, nowtime, oamount, sugg_amount;
    console.log("oic_calculator");
    admonth = myparseInt($('#id_pp_assessed_date_month').val()) - 1;
    adday = myparseInt($('#id_pp_assessed_date_day').val());
    adyear = myparseInt($('#id_pp_assessed_date_year').val());
    if (admonth === 0 || adday === 0 || adyear === 0) {
      $('.pp-calculation').hide();
    } else {
      expdate = new Date(adyear + 10, admonth, adday);
      nowtime = new Date();
      months = ((expdate - nowtime) / (1000 * 60 * 60 * 24 * 30.44)).toFixed();
      $('#pp_statute_exp_date').html((admonth + 1) + "-" + adday + "-" + (adyear + 10));
      $('#pp_statute_months_avail').html(months + " months");
      income = myparseInt($('#id_pp_monthly_income').val());
      debt = myparseInt($('#id_pp_debt_total').val());
      can_pay = months * income;
      $('#pp_can_pay').html("" + can_pay).keyup();
      if (can_pay < debt) {
        $('#pp_suggestion_qualify').html('MAY be');
      } else {
        $('#pp_suggestion_qualify').html('NOT');
      }
      sugg_amount = income * 12;
      $('#pp_suggested_amount').html("" + sugg_amount).keyup();
      oamount = myparseInt($('#id_pp_offer_amount').val());
      $('#id_pp_offer_amount').val(sugg_amount).keyup();
      $('.pp-calculation').show();
    }
    oic_calculator2();
    return true;
  };
  window.oic_calculator2 = function() {
    var cnt, i, initial_payment, j, oamount, remaining_balance, value;
    oamount = myparseInt($('#id_pp_offer_amount').val());
    console.log("oic_calculator2, oamount: " + oamount);
    if (!oamount || oamount === 0) {
      $('.pp-calculation2').hide();
    } else {
      initial_payment = (oamount / 5).toFixed();
      $('#pp_initial_payment').html(initial_payment).keyup();
      remaining_balance = oamount - initial_payment;
      cnt = 6;
      for (i = j = 1; j <= 5; i = ++j) {
        value = (remaining_balance / (cnt - i)).toFixed();
        remaining_balance = remaining_balance - value;
        $("#pp_payment_" + i).html(value).keyup();
      }
      $('.pp-calculation2').show();
    }
    return true;
  };
  $(document).on('keyup', '.oic-calculator input', function() {
    return oic_calculator();
  });
  $(document).on('change', '.oic-calculator input', function() {
    return oic_calculator();
  });
  $(document).on('change', '.oic-calculator select', function() {
    return oic_calculator();
  });
  $(document).on('keyup', '#id_pp_offer_amount', function() {
    return oic_calculator2();
  });
  return $(document).on('change', '#id_pp_offer_amount', function() {
    return oic_calculator2();
  });
});

},{}],"/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/paginationajax.js":[function(require,module,exports){
'use strict';
$(function() {
  var ascsort, curpage, disableEvents, navigate, ref, sortfield;
  curpage = 1;
  sortfield = $('.pagination-sortfield').data('field');
  ascsort = $('.pagination-sortfield').data('asc');
  if ((ref = "" + ascsort) !== '0' && ref !== '1') {
    ascsort = "1";
  }
  disableEvents = false;
  navigate = function(page) {
    var extravars, fname, fvalue, i, j, k, l, len, len1, len2, len3, lfilters, lfo, ref1, ref2, ref3, ref4;
    if (page == null) {
      page = null;
    }
    page = page || curpage;
    lfilters = "";
    ref1 = $('.input-filter');
    for (i = 0, len = ref1.length; i < len; i++) {
      lfo = ref1[i];
      fname = $(lfo).attr('name');
      fvalue = $(lfo).val();
      if (fvalue !== '-') {
        lfilters += "&filters[]=" + fname + "*" + fvalue;
      }
    }
    ref2 = $('.chk-filter');
    for (j = 0, len1 = ref2.length; j < len1; j++) {
      lfo = ref2[j];
      if ($(lfo).is(":checked")) {
        fname = $(lfo).attr('name');
        fvalue = $(lfo).val();
        if (fvalue !== '-') {
          lfilters += "&filters[]=" + fname + "*" + fvalue;
        }
      }
    }
    ref3 = $('.list-filter');
    for (k = 0, len2 = ref3.length; k < len2; k++) {
      lfo = ref3[k];
      fname = $(lfo).attr('name');
      fvalue = $(lfo).val();
      if (fvalue !== '-') {
        lfilters += "&filters[]=" + fname + "*" + fvalue;
      }
    }
    extravars = "";
    ref4 = $('.pagination-parameter');
    for (l = 0, len3 = ref4.length; l < len3; l++) {
      lfo = ref4[l];
      fname = $(lfo).data('name');
      fvalue = $(lfo).data('value');
      if (fvalue !== '-') {
        extravars += "&" + fname + "=" + fvalue;
      }
    }
    $.ajax(window.location.pathname + "?&page=" + page + lfilters + ("&sort=" + sortfield + "&asc=" + ascsort) + extravars, {
      type: 'GET',
      dataType: 'html',
      success: function(data, textStatus, jqXHR) {
        var hhh;
        curpage = page;
        $('.paginated_content').html(data);
        reinitWidgets();
        hhh = $("[data-sort='" + sortfield + "']").addClass('sortfield').html();
        if (("" + ascsort) === '1') {
          hhh = hhh.replace('</span></div>', ' <i class=" fa fa-sort-alpha-asc"></i></span></div>');
          return $("[data-sort='" + sortfield + "']").addClass('sortasc').html(hhh);
        } else {
          hhh = hhh.replace('</span></div>', ' <i class=" fa fa-sort-alpha-desc"></i></span></div>');
          return $("[data-sort='" + sortfield + "']").addClass('sortdesc').html(hhh);
        }
      }
    });
    return false;
  };
  window.navigate = navigate;
  $(document).on('click', '.listnav', function() {
    var nextpage;
    nextpage = $(this).data('page');
    if (!nextpage) {
      return false;
    }
    return navigate(nextpage);
  });
  $(document).on('change', '.list-filter', function() {
    if (!disableEvents) {
      return navigate(1);
    }
  });
  $(document).on('click', '.chk-filter', function() {
    if (!disableEvents) {
      navigate(1);
    }
    return true;
  });
  $(document).on('keyup', '.input-filter', function() {
    if (!disableEvents) {
      return navigate(1);
    }
  });
  $(document).on('click', '.filter-reset', function() {
    var i, j, len, len1, ref1, ref2, selobj;
    disableEvents = true;
    ref1 = $(".input-filter");
    for (i = 0, len = ref1.length; i < len; i++) {
      selobj = ref1[i];
      $(selobj).val('');
    }
    ref2 = $(".list-filter");
    for (j = 0, len1 = ref2.length; j < len1; j++) {
      selobj = ref2[j];
      $(selobj).select2('val', '-');
    }
    disableEvents = false;
    return navigate(1);
  });
  $(document).on('click', '[data-sort]', function() {
    var mysortfield;
    mysortfield = $(this).data('sort');
    if (sortfield === mysortfield) {
      ascsort = ascsort ^ 1;
    } else {
      ascsort = 1;
      sortfield = mysortfield;
    }
    return navigate();
  });
  if ($('.paginated_content').length > 0) {
    return navigate(1);
  }
});

},{}]},{},["/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/app_setup.js","/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/app.js","/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/client_cp.js","/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/irs_common.js","/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/irs433a.js","/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/irs656.js","/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/navigation.js","/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/oic_calc.js","/opt/projects/python/upwork.irsexpress.044/app/irsexpress2/dev/js/paginationajax.js"])
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi4uLy4uLy4uL25wbS9ub2RlX21vZHVsZXMvYnJvd3Nlci1wYWNrL19wcmVsdWRlLmpzIiwiaXJzZXhwcmVzczIvZGV2L2pzL2FwcC5qcyIsImlyc2V4cHJlc3MyL2Rldi9qcy9hcHBfc2V0dXAuanMiLCJpcnNleHByZXNzMi9kZXYvanMvY2xpZW50X2NwLmpzIiwiaXJzZXhwcmVzczIvZGV2L2pzL2lyczQzM2EuanMiLCJpcnNleHByZXNzMi9kZXYvanMvaXJzNjU2LmpzIiwiaXJzZXhwcmVzczIvZGV2L2pzL2lyc19jb21tb24uanMiLCJpcnNleHByZXNzMi9kZXYvanMvbmF2aWdhdGlvbi5qcyIsImlyc2V4cHJlc3MyL2Rldi9qcy9vaWNfY2FsYy5qcyIsImlyc2V4cHJlc3MyL2Rldi9qcy9wYWdpbmF0aW9uYWpheC5qcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTtBQ0FBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FDaE5BO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQ2ZBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQzdJQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FDNVJBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUMzR0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FDMVVBO0FBQ0E7QUFDQTs7QUNGQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUN0R0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EiLCJmaWxlIjoiZ2VuZXJhdGVkLmpzIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXNDb250ZW50IjpbIihmdW5jdGlvbiBlKHQsbixyKXtmdW5jdGlvbiBzKG8sdSl7aWYoIW5bb10pe2lmKCF0W29dKXt2YXIgYT10eXBlb2YgcmVxdWlyZT09XCJmdW5jdGlvblwiJiZyZXF1aXJlO2lmKCF1JiZhKXJldHVybiBhKG8sITApO2lmKGkpcmV0dXJuIGkobywhMCk7dmFyIGY9bmV3IEVycm9yKFwiQ2Fubm90IGZpbmQgbW9kdWxlICdcIitvK1wiJ1wiKTt0aHJvdyBmLmNvZGU9XCJNT0RVTEVfTk9UX0ZPVU5EXCIsZn12YXIgbD1uW29dPXtleHBvcnRzOnt9fTt0W29dWzBdLmNhbGwobC5leHBvcnRzLGZ1bmN0aW9uKGUpe3ZhciBuPXRbb11bMV1bZV07cmV0dXJuIHMobj9uOmUpfSxsLGwuZXhwb3J0cyxlLHQsbixyKX1yZXR1cm4gbltvXS5leHBvcnRzfXZhciBpPXR5cGVvZiByZXF1aXJlPT1cImZ1bmN0aW9uXCImJnJlcXVpcmU7Zm9yKHZhciBvPTA7bzxyLmxlbmd0aDtvKyspcyhyW29dKTtyZXR1cm4gc30pIiwiJ3VzZSBzdHJpY3QnO1xuJChmdW5jdGlvbigpIHtcbiAgdmFyIHNldF9zY3JvbGxhYmxlO1xuICB3aW5kb3cucGFzcyA9IGZ1bmN0aW9uKCkge1xuICAgIHJldHVybiBmYWxzZTtcbiAgfTtcbiAgd2luZG93Lm15cGFyc2VJbnQgPSBmdW5jdGlvbih2YWx1ZSkge1xuICAgIHZhciB2YWw7XG4gICAgdmFsID0gcGFyc2VJbnQodmFsdWUucmVwbGFjZSgvW1xcLixdL2csICcnKSk7XG4gICAgcmV0dXJuIHZhbDtcbiAgfTtcbiAgd2luZG93LndhaXRsb2FkX2xpc3QgPSB7fTtcbiAgd2luZG93LmNvbnRlbnRfbG9hZGVkID0gZnVuY3Rpb24obmFtZSkge1xuICAgIHZhciBhbGxfbG9hZGVkLCBpdGVtLCBub3Rsb2FkZWQ7XG4gICAgaWYgKG5hbWUpIHtcbiAgICAgIGNvbnNvbGUubG9nKG5hbWUgKyBcIiBsb2FkZWRcIik7XG4gICAgICB3YWl0bG9hZF9saXN0W25hbWVdID0gZmFsc2U7XG4gICAgfVxuICAgIGFsbF9sb2FkZWQgPSB0cnVlO1xuICAgIGZvciAoaXRlbSBpbiB3YWl0bG9hZF9saXN0KSB7XG4gICAgICBub3Rsb2FkZWQgPSB3YWl0bG9hZF9saXN0W2l0ZW1dO1xuICAgICAgaWYgKG5vdGxvYWRlZCkge1xuICAgICAgICBjb25zb2xlLmxvZyhcIndhaXRpbmcgZm9yIFwiICsgaXRlbSArIFwiIHRvIGJlIGxvYWRlZFwiKTtcbiAgICAgICAgYWxsX2xvYWRlZCA9IGZhbHNlO1xuICAgICAgICBicmVhaztcbiAgICAgIH1cbiAgICB9XG4gICAgaWYgKGFsbF9sb2FkZWQpIHtcbiAgICAgICQoJy5jb250ZW50LWxvYWQtd2FpdCcpLmVhY2goZnVuY3Rpb24oKSB7XG4gICAgICAgIHZhciBjZWxlbTtcbiAgICAgICAgY2VsZW0gPSAkKHRoaXMpLmRhdGEoJ2NvbnRlbnQtZWxlbWVudCcpO1xuICAgICAgICBpZiAoY2VsZW0pIHtcbiAgICAgICAgICAkKGNlbGVtKS5yZW1vdmVDbGFzcygnaGlkZGVuJyk7XG4gICAgICAgIH1cbiAgICAgICAgcmVpbml0V2lkZ2V0cygpO1xuICAgICAgICByZXR1cm4gJCh0aGlzKS5oaWRlKCk7XG4gICAgICB9KTtcbiAgICB9XG4gICAgcmV0dXJuIGZhbHNlO1xuICB9O1xuICB3aW5kb3cud2FpdHZhbGlkYXRpb25fbGlzdCA9IHt9O1xuICB3aW5kb3cudmFsaWRhdGluZ19mb3JtID0gXCJcIjtcbiAgd2luZG93LmZvcm1fdmFsaWRhdGVkID0gZnVuY3Rpb24obmFtZSwgcmVzdWx0KSB7XG4gICAgdmFyIGFsbF92YWxpZGF0ZWQsIGl0ZW0sIHZhbGlkYXRpb25fc3RhdGU7XG4gICAgaWYgKG5hbWUpIHtcbiAgICAgIGNvbnNvbGUubG9nKFwiZm9ybSBcIiArIG5hbWUgKyBcIiB2YWxpZGF0ZWQgKFwiICsgcmVzdWx0ICsgXCIpXCIpO1xuICAgICAgd2FpdHZhbGlkYXRpb25fbGlzdFtuYW1lXSA9IHJlc3VsdDtcbiAgICB9XG4gICAgYWxsX3ZhbGlkYXRlZCA9IHRydWU7XG4gICAgZm9yIChpdGVtIGluIHdhaXR2YWxpZGF0aW9uX2xpc3QpIHtcbiAgICAgIHZhbGlkYXRpb25fc3RhdGUgPSB3YWl0dmFsaWRhdGlvbl9saXN0W2l0ZW1dO1xuICAgICAgaWYgKHZhbGlkYXRpb25fc3RhdGUgPT09IDEpIHtcbiAgICAgICAgY29uc29sZS5sb2coXCJ3YWl0aW5nIGZvciBcIiArIGl0ZW0gKyBcIiB0byBiZSB2YWxpZGF0ZWRcIik7XG4gICAgICAgIGFsbF92YWxpZGF0ZWQgPSBmYWxzZTtcbiAgICAgICAgYnJlYWs7XG4gICAgICB9XG4gICAgICBpZiAodmFsaWRhdGlvbl9zdGF0ZSA9PT0gMikge1xuICAgICAgICBjb25zb2xlLmxvZyhcImZvcm0gXCIgKyBpdGVtICsgXCIgdmFsaWRhdGlvbiBmYWlsZWRcIik7XG4gICAgICAgIGFsbF92YWxpZGF0ZWQgPSBmYWxzZTtcbiAgICAgICAgJCgnLmZvcm0tdmFsaWRhdGlvbi13YWl0JykuaGlkZSgpO1xuICAgICAgICBicmVhaztcbiAgICAgIH1cbiAgICB9XG4gICAgaWYgKGFsbF92YWxpZGF0ZWQgJiYgd2luZG93LnZhbGlkYXRpbmdfZm9ybS5sZW5ndGggPiAwKSB7XG4gICAgICBjb25zb2xlLmxvZyhcInN1Ym1pdHRpbmcgZm9ybVwiKTtcbiAgICAgICQod2luZG93LnZhbGlkYXRpbmdfZm9ybSkuc3VibWl0KCk7XG4gICAgICByZXR1cm4gdHJ1ZTtcbiAgICB9XG4gIH07XG4gIHdpbmRvdy5yZWluaXRXaWRnZXRzID0gZnVuY3Rpb24oKSB7XG4gICAgJCgnLnRvZ2dsZS1jaGtib3gnKS5ib290c3RyYXBTd2l0Y2goKTtcbiAgICAkKCcuc3dpdGNoLXJhZGlvMicpLmJvb3RzdHJhcFN3aXRjaCgpO1xuICAgICQoJ3NlbGVjdCcpLnNlbGVjdDIoKTtcbiAgICAkKCcueHRvb2x0aXAnKS50b29sdGlwKCk7XG4gICAgcmV0dXJuICQoJ1tkYXRhLXRvZ2dsZT1cInBvcG92ZXJcIl0nKS5wb3BvdmVyKCk7XG4gIH07XG4gICQoJy5pbWctcG9wb3ZlcicpLnBvcG92ZXIoe1xuICAgIHRyaWdnZXI6ICdob3ZlcicsXG4gICAgcGxhY2VtZW50OiAncmlnaHQnLFxuICAgIGNvbnRlbnQ6IGZ1bmN0aW9uKCkge1xuICAgICAgcmV0dXJuICc8aW1nIHNyYz1cIicgKyAkKHRoaXMpLmRhdGEoJ3NyYycpICsgJ1wiPic7XG4gICAgfSxcbiAgICB0aXRsZTogXCJcIixcbiAgICBodG1sOiB0cnVlXG4gIH0pO1xuICByZWluaXRXaWRnZXRzKCk7XG4gICQoJy5mb3JtLWdyb3VwJykuZWFjaChmdW5jdGlvbigpIHtcbiAgICB2YXIgZXJyb3JfbWVzc2FnZXM7XG4gICAgZXJyb3JfbWVzc2FnZXMgPSAkKHRoaXMpLmF0dHIoJ2Vycm9yX21lc3NhZ2VzJyk7XG4gICAgaWYgKGVycm9yX21lc3NhZ2VzKSB7XG4gICAgICAkKHRoaXMpLmFkZENsYXNzKCdoYXMtZXJyb3InKTtcbiAgICAgICQoJ2lucHV0JywgdGhpcykucG9wb3Zlcih7XG4gICAgICAgIHBsYWNlbWVudDogJ3JpZ2h0JyxcbiAgICAgICAgY29udGVudDogZnVuY3Rpb24oKSB7XG4gICAgICAgICAgcmV0dXJuICc8c3BhbiBjbGFzcz1cInRleHQtZGFuZ2VyXCI+JyArIGVycm9yX21lc3NhZ2VzICsgJzwvc3Bhbj4nO1xuICAgICAgICB9LFxuICAgICAgICB0aXRsZTogXCJcIixcbiAgICAgICAgaHRtbDogdHJ1ZVxuICAgICAgfSk7XG4gICAgICByZXR1cm4gJCgnaW5wdXQnLCB0aGlzKS5wb3BvdmVyKCdzaG93Jyk7XG4gICAgfVxuICB9KTtcbiAgc2V0X3Njcm9sbGFibGUgPSBmdW5jdGlvbigpIHtcbiAgICB2YXIgY29udGVudF9oZWlnaHQsIHdpbmRvd19oZWlnaHQ7XG4gICAgd2luZG93X2hlaWdodCA9ICQoZG9jdW1lbnQpLmhlaWdodCgpO1xuICAgIGNvbnRlbnRfaGVpZ2h0ID0gd2luZG93X2hlaWdodCAtIDMwMDtcbiAgICByZXR1cm4gJCgnLnNjcm9sbGFibGUnKS5oZWlnaHQoY29udGVudF9oZWlnaHQpO1xuICB9O1xuICAkKHdpbmRvdykucmVzaXplKHNldF9zY3JvbGxhYmxlKTtcbiAgc2V0X3Njcm9sbGFibGUoKTtcbiAgJChkb2N1bWVudCkub24oXCJjbGlja1wiLCBcIi5zaW1wbGUtYWpheC1idG5cIiwgZnVuY3Rpb24oKSB7XG4gICAgdmFyIG1ldGhvZCwgb25zdWNjZXNzLCB1cmw7XG4gICAgdXJsID0gJCh0aGlzKS5kYXRhKCd1cmwnKTtcbiAgICBtZXRob2QgPSAkKHRoaXMpLmRhdGEoJ21ldGhvZCcpO1xuICAgIGlmICghbWV0aG9kKSB7XG4gICAgICBtZXRob2QgPSAnR0VUJztcbiAgICB9XG4gICAgb25zdWNjZXNzID0gJCh0aGlzKS5kYXRhKCdvbnN1Y2Nlc3MnKTtcbiAgICAkLmFqYXgodXJsLCB7XG4gICAgICB0eXBlOiBtZXRob2QsXG4gICAgICBkYXRhVHlwZTogJ2h0bWwnLFxuICAgICAgc3VjY2VzczogZnVuY3Rpb24oZGF0YSwgdGV4dFN0YXR1cywganFYSFIpIHtcbiAgICAgICAgaWYgKG9uc3VjY2VzcyA9PT0gJ3JlZnJlc2gnKSB7XG4gICAgICAgICAgbG9jYXRpb24ucmVsb2FkKHRydWUpO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiBmYWxzZTtcbiAgICAgIH1cbiAgICB9KTtcbiAgICByZXR1cm4gZmFsc2U7XG4gIH0pO1xuICAkKGRvY3VtZW50KS5vbihcImNsaWNrXCIsIFwiLmRpc2FibGVkXCIsIGZ1bmN0aW9uKCkge1xuICAgIHJldHVybiBmYWxzZTtcbiAgfSk7XG4gIHdpbmRvdy5jaGtyYWRpb19zZW1hZm9yID0gZmFsc2U7XG4gICQoZG9jdW1lbnQpLm9uKCdzd2l0Y2hDaGFuZ2UuYm9vdHN0cmFwU3dpdGNoJywgXCIuY2hrLXJhZGlvZ3JvdXBcIiwgZnVuY3Rpb24oZXZlbnQsIHN0YXRlKSB7XG4gICAgdmFyIG5hbWUsIHJhZGlvZ3JvdXA7XG4gICAgaWYgKHdpbmRvdy5jaGtyYWRpb19zZW1hZm9yKSB7XG4gICAgICByZXR1cm4gdHJ1ZTtcbiAgICB9XG4gICAgaWYgKCFzdGF0ZSkge1xuICAgICAgcmV0dXJuIHRydWU7XG4gICAgfVxuICAgIHdpbmRvdy5jaGtyYWRpb19zZW1hZm9yID0gdHJ1ZTtcbiAgICByYWRpb2dyb3VwID0gJCh0aGlzKS5kYXRhKCdyYWRpb2dyb3VwJyk7XG4gICAgbmFtZSA9ICQodGhpcykuYXR0cignbmFtZScpO1xuICAgICQoXCIuXCIgKyByYWRpb2dyb3VwKS5lYWNoKGZ1bmN0aW9uKCkge1xuICAgICAgdmFyIHRoaXNuYW1lO1xuICAgICAgdGhpc25hbWUgPSAkKHRoaXMpLmF0dHIoJ25hbWUnKTtcbiAgICAgIGlmICh0aGlzbmFtZSAhPT0gbmFtZSkge1xuICAgICAgICAkKHRoaXMpLmRhdGEoXCJib290c3RyYXAtc3dpdGNoXCIpLnN0YXRlKGZhbHNlKTtcbiAgICAgIH1cbiAgICAgIHJldHVybiB0cnVlO1xuICAgIH0pO1xuICAgIHdpbmRvdy5jaGtyYWRpb19zZW1hZm9yID0gZmFsc2U7XG4gICAgcmV0dXJuIHRydWU7XG4gIH0pO1xuICBzZXRUaW1lb3V0KGNvbnRlbnRfbG9hZGVkLCAxMDAwKTtcbiAgd2luZG93Lm1hc2tfbnVtID0gZnVuY3Rpb24oc2VsZWN0b3IpIHtcbiAgICAkKHNlbGVjdG9yKS51bm1hc2soKTtcbiAgICAkKHNlbGVjdG9yKS5tYXNrKCcjLCMjMCcsIHtcbiAgICAgIHJldmVyc2U6IHRydWUsXG4gICAgICB0cmFuc2xhdGlvbjoge1xuICAgICAgICAnIyc6IHtcbiAgICAgICAgICBwYXR0ZXJuOiAvLXxcXGQvLFxuICAgICAgICAgIHJlY3Vyc2l2ZTogdHJ1ZVxuICAgICAgICB9XG4gICAgICB9LFxuICAgICAgb25DaGFuZ2U6IGZ1bmN0aW9uKHZhbHVlLCBlKSB7XG4gICAgICAgIHZhciBuZXd2YWx1ZSwgcG9zaXRpb24sIHRhZywgdGFyZ2V0O1xuICAgICAgICB0YXJnZXQgPSBlLnRhcmdldDtcbiAgICAgICAgdGFnID0gJCh0YXJnZXQpLnByb3AoXCJ0YWdOYW1lXCIpO1xuICAgICAgICBuZXd2YWx1ZSA9IHZhbHVlLnJlcGxhY2UoLyg/IV4pLS9nLCAnJykucmVwbGFjZSgvXiwvLCAnJykucmVwbGFjZSgvXi0sLywgJy0nKTtcbiAgICAgICAgaWYgKHRhZyA9PT0gJ0lOUFVUJykge1xuICAgICAgICAgIGlmICgkKHRhcmdldCkuaXMoJzpmb2N1cycpKSB7XG4gICAgICAgICAgICBwb3NpdGlvbiA9IHRhcmdldC5zZWxlY3Rpb25TdGFydDtcbiAgICAgICAgICAgIHRhcmdldC52YWx1ZSA9IG5ld3ZhbHVlO1xuICAgICAgICAgICAgdGFyZ2V0LnNlbGVjdGlvbkVuZCA9IHBvc2l0aW9uO1xuICAgICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICB0YXJnZXQudmFsdWUgPSBuZXd2YWx1ZTtcbiAgICAgICAgICB9XG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgdGFyZ2V0LmlubmVySFRNTCA9IG5ld3ZhbHVlO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiB0cnVlO1xuICAgICAgfVxuICAgIH0pO1xuICAgIHJldHVybiB0cnVlO1xuICB9O1xuICAkKCdpbnB1dFt0eXBlPVwidGVsXCJdJykubWFzaygnMDAwLTAwMC0wMDAwJyk7XG4gICQoJ2lucHV0Lm51bWJlci1maWVsZC5wb3NpdGl2ZS1udW1iZXInKS5tYXNrKCcjLCMjMCcsIHtcbiAgICAncmV2ZXJzZSc6IHRydWVcbiAgfSk7XG4gIG1hc2tfbnVtKCdpbnB1dC5udW1iZXItZmllbGQuYWxsb3ctbmVnYXRpdmUnKTtcbiAgbWFza19udW0oJ3NwYW4ubnVtYmVyLWZpZWxkJyk7XG4gICQoJ2lucHV0LnllYXItZmllbGQnKS5tYXNrKCcwMDAwJywge1xuICAgICdyZXZlcnNlJzogdHJ1ZVxuICB9KTtcbiAgJCgnaW5wdXQuZmxvYXQtZmllbGQnKS5tYXNrKCcjLCMjMC4wMCcsIHtcbiAgICAncmV2ZXJzZSc6IHRydWVcbiAgfSk7XG4gICQoJ2lucHV0LnppcC1maWVsZCcpLm1hc2soJzAwMDAwMCcpO1xuICAkKCdpbnB1dC5zc24tZmllbGQnKS5tYXNrKCcwMDAtMDAtMDAwMCcpO1xuICAkKCdpbnB1dC5jYWYtZmllbGQnKS5tYXNrKCcwMDAwLTAwMDAwJyk7XG4gICQoJ2lucHV0LnB0aW4tZmllbGQnKS5tYXNrKCcwMDAwMDAwMCcpO1xuICAkKCdpbnB1dCNpZF9yb3V0aW5nX251bWJlcicpLm1hc2soJzAwMDAwMDAwMDAnKTtcbiAgJCgnaW5wdXQjaWRfYWNjb3VudF9udW1iZXInKS5tYXNrKCcwMDAwMDAwMDAwMDAwMDAwMCcpO1xuICByZXR1cm4gJCgnLmp1c3R5ZWFycyBpbnB1dCcpLm1hc2soJzAwMDAnKTtcbn0pO1xuIiwiJ3VzZSBzdHJpY3QnO1xuJChmdW5jdGlvbigpIHtcbiAgdmFyIGNzcmZTYWZlTWV0aG9kLCBjc3JmdG9rZW47XG4gIGNzcmZ0b2tlbiA9IENvb2tpZXMuZ2V0KCdjc3JmdG9rZW4nKTtcbiAgY3NyZlNhZmVNZXRob2QgPSBmdW5jdGlvbihtZXRob2QpIHtcbiAgICByZXR1cm4gL14oR0VUfEhFQUR8T1BUSU9OU3xUUkFDRSkkLy50ZXN0KG1ldGhvZCk7XG4gIH07XG4gIHJldHVybiAkLmFqYXhTZXR1cCh7XG4gICAgYmVmb3JlU2VuZDogZnVuY3Rpb24oeGhyLCBzZXR0aW5ncykge1xuICAgICAgaWYgKCFjc3JmU2FmZU1ldGhvZChzZXR0aW5ncy50eXBlKSAmJiAhdGhpcy5jcm9zc0RvbWFpbikge1xuICAgICAgICByZXR1cm4geGhyLnNldFJlcXVlc3RIZWFkZXIoXCJYLUNTUkZUb2tlblwiLCBjc3JmdG9rZW4pO1xuICAgICAgfVxuICAgIH1cbiAgfSk7XG59KTtcbiIsIid1c2Ugc3RyaWN0JztcbiQoZnVuY3Rpb24oKSB7XG4gIHdpbmRvdy5yZWxvYWRfYWpheCA9IGZ1bmN0aW9uKHNlbGVjdG9yKSB7XG4gICAgdmFyIHVybDtcbiAgICB1cmwgPSAkKHNlbGVjdG9yKS5kYXRhKCdzcmMnKTtcbiAgICAkLmFqYXgodXJsLCB7XG4gICAgICB0eXBlOiAnR0VUJyxcbiAgICAgIGRhdGFUeXBlOiAnaHRtbCcsXG4gICAgICBzdWNjZXNzOiBmdW5jdGlvbihkYXRhLCB0ZXh0U3RhdHVzLCBqcVhIUikge1xuICAgICAgICByZXR1cm4gJChzZWxlY3RvcikuaHRtbChkYXRhKTtcbiAgICAgIH1cbiAgICB9KTtcbiAgICByZXR1cm4gZmFsc2U7XG4gIH07XG4gIHdpbmRvdy5jbGllbnRfdXBkYXRlID0gZnVuY3Rpb24oY2xpZW50X2RhdGEsIG9uc3VjY2Vzcykge1xuICAgIHZhciBjbGllbnRfaWQsIGNzcmZ0b2tlbiwgdXJsO1xuICAgIGNsaWVudF9pZCA9ICQoJyNvYmplY3RfZGF0YScpLmRhdGEoJ29iamVjdGlkJyk7XG4gICAgdXJsID0gJCgnLmNwLWNvbnRlbnQnKS5kYXRhKCdzcmMnKTtcbiAgICBjc3JmdG9rZW4gPSBDb29raWVzLmdldCgnY3NyZnRva2VuJyk7XG4gICAgJC5hamF4KHVybCwge1xuICAgICAgdHlwZTogJ1BVVCcsXG4gICAgICBkYXRhVHlwZTogJ2pzb24nLFxuICAgICAgY29udGVudFR5cGU6IFwiYXBwbGljYXRpb24vanNvblwiLFxuICAgICAgZGF0YTogSlNPTi5zdHJpbmdpZnkoY2xpZW50X2RhdGEpLFxuICAgICAgc3VjY2Vzczogb25zdWNjZXNzXG4gICAgfSk7XG4gICAgcmV0dXJuIGZhbHNlO1xuICB9O1xuICAkKCcuY2xpZW50LWRlbGV0ZS1idG4nKS5jbGljayhmdW5jdGlvbigpIHtcbiAgICB2YXIgc3VjY2Vzc191cmwsIHVybDtcbiAgICBpZiAoY29uZmlybShcIkFyZSB5b3Ugc3VyZSB5b3Ugd2FudCB0byBkZWxldGUgdGhpcyBpdGVtP1xcblRoaXMgb3BlcmF0aW9uIGNhbm5vdCBiZSB1bmRvbmUhXCIpKSB7XG4gICAgICB1cmwgPSAkKHRoaXMpLmRhdGEoJ3VybCcpO1xuICAgICAgc3VjY2Vzc191cmwgPSAkKHRoaXMpLmRhdGEoJ3N1Y2Nlc3MtdXJsJyk7XG4gICAgICAkLmFqYXgodXJsLCB7XG4gICAgICAgIHR5cGU6ICdQT1NUJyxcbiAgICAgICAgc3VjY2VzczogZnVuY3Rpb24oZGF0YSwgdGV4dFN0YXR1cywganFYSFIpIHtcbiAgICAgICAgICB3aW5kb3cubG9jYXRpb24uaHJlZiA9IHN1Y2Nlc3NfdXJsO1xuICAgICAgICAgIHJldHVybiBmYWxzZTtcbiAgICAgICAgfVxuICAgICAgfSk7XG4gICAgfVxuICAgIHJldHVybiBmYWxzZTtcbiAgfSk7XG4gICQoJy5jbGllbnQtc3RhdHVzLWJ0bicpLmNsaWNrKGZ1bmN0aW9uKCkge1xuICAgIHZhciBlbGVtZW50LCBuZXdzdGF0dXM7XG4gICAgZWxlbWVudCA9IHRoaXM7XG4gICAgJCgnLmNsaWVudC1zdGF0dXMtYnRuJykucmVtb3ZlQ2xhc3MoJ2FjdGl2ZScpO1xuICAgICQoJy5jbGllbnQtc3RhdHVzLWJ0biBzcGFuLmZhJykucmVtb3ZlQ2xhc3MoJ2ZhLWNoZWNrJyk7XG4gICAgbmV3c3RhdHVzID0gJCh0aGlzKS5kYXRhKCdzdGF0dXMnKTtcbiAgICBjbGllbnRfdXBkYXRlKHtcbiAgICAgICdzdGF0dXMnOiBuZXdzdGF0dXNcbiAgICB9LCBmdW5jdGlvbihkYXRhLCB0ZXh0U3RhdHVzLCBqcVhIUikge1xuICAgICAgcmVsb2FkX2FqYXgoJy5jcC1jb250ZW50Jyk7XG4gICAgICAkKGVsZW1lbnQpLmFkZENsYXNzKCdhY3RpdmUnKTtcbiAgICAgIHJldHVybiAkKCdzcGFuLmZhJywgZWxlbWVudCkuYWRkQ2xhc3MoJ2ZhLWNoZWNrJyk7XG4gICAgfSk7XG4gICAgcmV0dXJuIGZhbHNlO1xuICB9KTtcbiAgd2luZG93LmNsaWVudF9zdW1tYXJ5X2NoYW5nZSA9IGZ1bmN0aW9uKCkge1xuICAgIGlmICgkKCcjY2xpZW50X3N1bW1hcnknKS52YWwoKSAhPT0gJCgnI2NsaWVudF9zdW1tYXJ5X3NhdmVkJykudmFsKCkpIHtcbiAgICAgICQoJy5zdW1tYXJ5LXNhdmVkLWluZGljYXRvcicpLmhpZGUoKTtcbiAgICAgIHJldHVybiAkKCcuc3VtbWFyeS1ub3RzYXZlZC1pbmRpY2F0b3InKS5zaG93KCk7XG4gICAgfSBlbHNlIHtcbiAgICAgICQoJy5zdW1tYXJ5LXNhdmVkLWluZGljYXRvcicpLnNob3coKTtcbiAgICAgIHJldHVybiAkKCcuc3VtbWFyeS1ub3RzYXZlZC1pbmRpY2F0b3InKS5oaWRlKCk7XG4gICAgfVxuICB9O1xuICAkKCcjY2xpZW50X3N1bW1hcnknKS5jaGFuZ2UoZnVuY3Rpb24oKSB7XG4gICAgcmV0dXJuIGNsaWVudF9zdW1tYXJ5X2NoYW5nZSgpO1xuICB9KTtcbiAgJCgnI2NsaWVudF9zdW1tYXJ5Jykua2V5dXAoZnVuY3Rpb24oKSB7XG4gICAgcmV0dXJuIGNsaWVudF9zdW1tYXJ5X2NoYW5nZSgpO1xuICB9KTtcbiAgJCgnLnN1bW1hcnktc2F2ZS1idG4nKS5jbGljayhmdW5jdGlvbigpIHtcbiAgICB2YXIgc3VtbWFyeV9kYXRhO1xuICAgIHN1bW1hcnlfZGF0YSA9ICQoXCIjY2xpZW50X3N1bW1hcnlcIikudmFsKCk7XG4gICAgY2xpZW50X3VwZGF0ZSh7XG4gICAgICAnc3VtbWFyeSc6IHN1bW1hcnlfZGF0YVxuICAgIH0sIGZ1bmN0aW9uKGRhdGEsIHRleHRTdGF0dXMsIGpxWEhSKSB7XG4gICAgICAkKCcjY2xpZW50X3N1bW1hcnlfc2F2ZWQnKS52YWwoJCgnI2NsaWVudF9zdW1tYXJ5JykudmFsKCkpO1xuICAgICAgcmV0dXJuIGNsaWVudF9zdW1tYXJ5X2NoYW5nZSgpO1xuICAgIH0pO1xuICAgIHJldHVybiBmYWxzZTtcbiAgfSk7XG4gICQoJy5zdW1tYXJ5LW5vdHNhdmVkLWluZGljYXRvcicpLnJlbW92ZUNsYXNzKCdoaWRkZW4nKTtcbiAgJCgnLnN1bW1hcnktbm90c2F2ZWQtaW5kaWNhdG9yJykuaGlkZSgpO1xuICAkKCcuc3VtbWFyeS1zYXZlZC1pbmRpY2F0b3InKS5yZW1vdmVDbGFzcygnaGlkZGVuJyk7XG4gICQoJ2J1dHRvbi5wZGZlZGl0LWJ0bicpLmNsaWNrKGZ1bmN0aW9uKCkge1xuICAgIGFsZXJ0KFwiTm90IGltcGxlbWVudGVkIHlldCwgc29ycnlcIik7XG4gICAgcmV0dXJuIGZhbHNlO1xuICB9KTtcbiAgJChkb2N1bWVudCkub24oXCJjbGlja1wiLCAnLmVkaXQtbm90ZWRvYy1idG4nLCBmdW5jdGlvbigpIHtcbiAgICB2YXIgbW9kYWxmb3JtLCB1cmw7XG4gICAgdXJsID0gJCh0aGlzKS5kYXRhKCd1cmwnKTtcbiAgICBtb2RhbGZvcm0gPSAkKFwiLm1vZGFsLWVsZW1lbnRcIik7XG4gICAgJC5hamF4KHVybCwge1xuICAgICAgdHlwZTogJ0dFVCcsXG4gICAgICBkYXRhVHlwZTogJ2h0bWwnLFxuICAgICAgc3VjY2VzczogZnVuY3Rpb24oZGF0YSwgdGV4dFN0YXR1cywganFYSFIpIHtcbiAgICAgICAgJChtb2RhbGZvcm0pLmh0bWwoZGF0YSk7XG4gICAgICAgIHJlaW5pdFdpZGdldHMoKTtcbiAgICAgICAgJCgnLm1vZGFsZm9ybScsIG1vZGFsZm9ybSkubW9kYWwoJ3Nob3cnKTtcbiAgICAgICAgcmV0dXJuICQoJy5mb3Jtc2F2ZWJ0bicsIG1vZGFsZm9ybSkuY2xpY2soZnVuY3Rpb24oKSB7XG4gICAgICAgICAgJCgnZm9ybScsIG1vZGFsZm9ybSkuYWpheFN1Ym1pdCgpO1xuICAgICAgICAgICQoJy5tb2RhbGZvcm0nLCBtb2RhbGZvcm0pLm1vZGFsKCdoaWRlJyk7XG4gICAgICAgICAgcmV0dXJuIHJlbG9hZF9hamF4KCcubm90ZXMtbGlzdCcpO1xuICAgICAgICB9KTtcbiAgICAgIH1cbiAgICB9KTtcbiAgICByZXR1cm4gZmFsc2U7XG4gIH0pO1xuICAkKGRvY3VtZW50KS5vbihcImNsaWNrXCIsICcuZGVsZXRlLW5vdGVkb2MtYnRuJywgZnVuY3Rpb24oKSB7XG4gICAgdmFyIGNhbl9kZWxldGUsIHVybDtcbiAgICB1cmwgPSAkKHRoaXMpLmRhdGEoJ3VybCcpO1xuICAgIGNhbl9kZWxldGUgPSBjb25maXJtKFwiQXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGRlbGV0ZSB0aGlzIGVsZW1lbnQ/XCIpO1xuICAgIGlmICghY2FuX2RlbGV0ZSkge1xuICAgICAgcmV0dXJuIGZhbHNlO1xuICAgIH1cbiAgICAkLmFqYXgodXJsLCB7XG4gICAgICB0eXBlOiAnREVMRVRFJyxcbiAgICAgIGRhdGFUeXBlOiAnaHRtbCcsXG4gICAgICBzdWNjZXNzOiBmdW5jdGlvbihkYXRhLCB0ZXh0U3RhdHVzLCBqcVhIUikge1xuICAgICAgICByZWxvYWRfYWpheCgnLm5vdGVzLWxpc3QnKTtcbiAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgICAgfVxuICAgIH0pO1xuICAgIHJldHVybiBmYWxzZTtcbiAgfSk7XG4gIHJldHVybiAkKGRvY3VtZW50KS5vbihcImNsaWNrXCIsICcuc3RhZ2VidG4nLCBmdW5jdGlvbigpIHtcbiAgICB2YXIgbmV3c3RhZ2U7XG4gICAgbmV3c3RhZ2UgPSAkKHRoaXMpLmRhdGEoJ25ld3N0YWdlJyk7XG4gICAgY2xpZW50X3VwZGF0ZSh7XG4gICAgICAnc3RhZ2UnOiBuZXdzdGFnZVxuICAgIH0sIGZ1bmN0aW9uKGRhdGEsIHRleHRTdGF0dXMsIGpxWEhSKSB7XG4gICAgICByZWxvYWRfYWpheCgnLmNwLWNvbnRlbnQnKTtcbiAgICAgIHJlbG9hZF9hamF4KCcubm90ZXMtbGlzdCcpO1xuICAgICAgcmV0dXJuIGZhbHNlO1xuICAgIH0pO1xuICAgIHJldHVybiBmYWxzZTtcbiAgfSk7XG59KTtcbiIsIid1c2Ugc3RyaWN0JztcbiQoZnVuY3Rpb24oKSB7XG4gIHZhciBkYXRhLCBlbGVtZW50LCBmb3JtNDMzYV9wYWdlLCBpLCBsZW4sIHN1Z2csIHN1Z2dlc3Rpb25zO1xuICBmb3JtNDMzYV9wYWdlID0gJCgnLjQzM0EtcGFnZWFjdGl2ZScpLmRhdGEoJ3ZhbHVlJyk7XG4gIGlmIChmb3JtNDMzYV9wYWdlID09PSAnaXNfcGFnZTRfYWN0aXZlJykge1xuICAgICQoZG9jdW1lbnQpLm9uKFwia2V5dXBcIiwgXCIuZm9ybTQzM2EgLmFjY291bnRfYmFsYW5jZVwiLCBmdW5jdGlvbigpIHtcbiAgICAgIHZhciBzdW07XG4gICAgICBzdW0gPSAwO1xuICAgICAgJChcIi5mb3JtNDMzYSAuYWNjb3VudF9iYWxhbmNlXCIpLmVhY2goZnVuY3Rpb24oKSB7XG4gICAgICAgIHN1bSArPSBteXBhcnNlSW50KCQodGhpcykudmFsKCkpO1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH0pO1xuICAgICAgcmV0dXJuICQoXCIuZm9ybTQzM2EgI2lkX3RvdGFsX2Nhc2hcIikudmFsKHN1bSkua2V5dXAoKTtcbiAgICB9KTtcbiAgICAkKGRvY3VtZW50KS5vbihcImtleXVwXCIsIFwiLmZvcm00MzNhIC5sb2FuX2JhbGFuY2VfY3VydmFsXCIsIGZ1bmN0aW9uKCkge1xuICAgICAgdmFyIGN2LCBlcXVpdHksIGxiO1xuICAgICAgbGIgPSBjdiA9IDA7XG4gICAgICAkKFwiLmZvcm00MzNhIC5sb2FuX2JhbGFuY2VcIikuZWFjaChmdW5jdGlvbigpIHtcbiAgICAgICAgbGIgKz0gbXlwYXJzZUludCgkKHRoaXMpLnZhbCgpKTtcbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICB9KTtcbiAgICAgICQoXCIuZm9ybTQzM2EgLmN1cnJlbnRfdmFsdWVcIikuZWFjaChmdW5jdGlvbigpIHtcbiAgICAgICAgY3YgKz0gbXlwYXJzZUludCgkKHRoaXMpLnZhbCgpKTtcbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICB9KTtcbiAgICAgIGVxdWl0eSA9IGN2IC0gbGI7XG4gICAgICByZXR1cm4gJChcIi5mb3JtNDMzYSAjaWRfdG90YWxfZXF1aXR5XCIpLnZhbChlcXVpdHkpLmtleXVwKCk7XG4gICAgfSk7XG4gICAgJChkb2N1bWVudCkub24oXCJrZXl1cFwiLCBcIi5mb3JtNDMzYSAuYW1vdW50X293ZWRfY3JsaW1pdFwiLCBmdW5jdGlvbigpIHtcbiAgICAgIHZhciBhbywgY2wsIHRvdGFsX2NyZWRpdDtcbiAgICAgIGFvID0gY2wgPSAwO1xuICAgICAgJChcIi5mb3JtNDMzYSAuYW1vdW50X293ZWRcIikuZWFjaChmdW5jdGlvbigpIHtcbiAgICAgICAgYW8gKz0gbXlwYXJzZUludCgkKHRoaXMpLnZhbCgpKTtcbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICB9KTtcbiAgICAgICQoXCIuZm9ybTQzM2EgLmNyZWRpdF9saW1pdFwiKS5lYWNoKGZ1bmN0aW9uKCkge1xuICAgICAgICBjbCArPSBteXBhcnNlSW50KCQodGhpcykudmFsKCkpO1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH0pO1xuICAgICAgdG90YWxfY3JlZGl0ID0gY2wgLSBhbztcbiAgICAgIHJldHVybiAkKFwiLmZvcm00MzNhICNpZF90b3RhbF9jcmVkaXRcIikudmFsKHRvdGFsX2NyZWRpdCkua2V5dXAoKTtcbiAgICB9KTtcbiAgICAkKGRvY3VtZW50KS5vbihcImtleXVwXCIsIFwiLmZvcm00MzNhIC5jYXNoX3ZhbHVlX2xiYWxcIiwgZnVuY3Rpb24oKSB7XG4gICAgICB2YXIgYWNhc2gsIGN2LCBsYjtcbiAgICAgIGxiID0gY3YgPSAwO1xuICAgICAgJChcIi5mb3JtNDMzYSAuaWlsb2FuX2JhbGFuY2VcIikuZWFjaChmdW5jdGlvbigpIHtcbiAgICAgICAgbGIgKz0gbXlwYXJzZUludCgkKHRoaXMpLnZhbCgpKTtcbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICB9KTtcbiAgICAgICQoXCIuZm9ybTQzM2EgLmNhc2hfdmFsdWVcIikuZWFjaChmdW5jdGlvbigpIHtcbiAgICAgICAgY3YgKz0gbXlwYXJzZUludCgkKHRoaXMpLnZhbCgpKTtcbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICB9KTtcbiAgICAgIGFjYXNoID0gY3YgLSBsYjtcbiAgICAgIHJldHVybiAkKFwiLmZvcm00MzNhICNpZF90b3RhbF9hdmFpbGFibGVfY2FzaFwiKS52YWwoYWNhc2gpLmtleXVwKCk7XG4gICAgfSk7XG4gIH1cbiAgaWYgKGZvcm00MzNhX3BhZ2UgPT09ICdpc19wYWdlNV9hY3RpdmUnKSB7XG4gICAgJChkb2N1bWVudCkub24oXCJrZXl1cFwiLCBcIi5mb3JtNDMzYSAucnBmbXZfY2xiXCIsIGZ1bmN0aW9uKCkge1xuICAgICAgdmFyIGVxdWl0eSwgbGIsIG12O1xuICAgICAgbGIgPSBtdiA9IDA7XG4gICAgICAkKFwiLmZvcm00MzNhIC5ycGN1cnJlbnRfbG9hbl9iYWxhbmNlXCIpLmVhY2goZnVuY3Rpb24oKSB7XG4gICAgICAgIGxiICs9IG15cGFyc2VJbnQoJCh0aGlzKS52YWwoKSk7XG4gICAgICAgIHJldHVybiB0cnVlO1xuICAgICAgfSk7XG4gICAgICAkKFwiLmZvcm00MzNhIC5ycG1hcmtldF92YWx1ZVwiKS5lYWNoKGZ1bmN0aW9uKCkge1xuICAgICAgICBtdiArPSBteXBhcnNlSW50KCQodGhpcykudmFsKCkpO1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH0pO1xuICAgICAgZXF1aXR5ID0gbXYgLSBsYjtcbiAgICAgIHJldHVybiAkKFwiLmZvcm00MzNhICNpZF9yZWFsX3Byb3BlcnR5X3RvdGFsX2VxdWl0eVwiKS52YWwoZXF1aXR5KS5rZXl1cCgpO1xuICAgIH0pO1xuICAgICQoZG9jdW1lbnQpLm9uKFwia2V5dXBcIiwgXCIuZm9ybTQzM2EgLnZ2Zm12X2NsYlwiLCBmdW5jdGlvbigpIHtcbiAgICAgIHZhciBlcXVpdHksIGxiLCBtdjtcbiAgICAgIGxiID0gbXYgPSAwO1xuICAgICAgJChcIi5mb3JtNDMzYSAudnZjdXJyZW50X2xvYW5fYmFsYW5jZVwiKS5lYWNoKGZ1bmN0aW9uKCkge1xuICAgICAgICBsYiArPSBteXBhcnNlSW50KCQodGhpcykudmFsKCkpO1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH0pO1xuICAgICAgJChcIi5mb3JtNDMzYSAudnZtYXJrZXRfdmFsdWVcIikuZWFjaChmdW5jdGlvbigpIHtcbiAgICAgICAgbXYgKz0gbXlwYXJzZUludCgkKHRoaXMpLnZhbCgpKTtcbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICB9KTtcbiAgICAgIGVxdWl0eSA9IG12IC0gbGI7XG4gICAgICByZXR1cm4gJChcIi5mb3JtNDMzYSAjaWRfdmVoaWNsZXNfdG90YWxfZXF1aXR5XCIpLnZhbChlcXVpdHkpLmtleXVwKCk7XG4gICAgfSk7XG4gICAgJChkb2N1bWVudCkub24oXCJrZXl1cFwiLCBcIi5mb3JtNDMzYSAucGFmbXZfY2xiXCIsIGZ1bmN0aW9uKCkge1xuICAgICAgdmFyIGVxdWl0eSwgbGIsIG12O1xuICAgICAgbGIgPSBtdiA9IDA7XG4gICAgICAkKFwiLmZvcm00MzNhIC5wYWN1cnJlbnRfbG9hbl9iYWxhbmNlXCIpLmVhY2goZnVuY3Rpb24oKSB7XG4gICAgICAgIGxiICs9IG15cGFyc2VJbnQoJCh0aGlzKS52YWwoKSk7XG4gICAgICAgIHJldHVybiB0cnVlO1xuICAgICAgfSk7XG4gICAgICAkKFwiLmZvcm00MzNhIC5wYW1hcmtldF92YWx1ZVwiKS5lYWNoKGZ1bmN0aW9uKCkge1xuICAgICAgICBtdiArPSBteXBhcnNlSW50KCQodGhpcykudmFsKCkpO1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH0pO1xuICAgICAgZXF1aXR5ID0gbXYgLSBsYjtcbiAgICAgIHJldHVybiAkKFwiLmZvcm00MzNhICNpZF9wZXJzb25hbF9hc3NldHNfdG90YWxfZXF1aXR5XCIpLnZhbChlcXVpdHkpLmtleXVwKCk7XG4gICAgfSk7XG4gICAgJChkb2N1bWVudCkub24oXCJjbGlja1wiLCBcIi5mb3JtNDMzYSAucGEtc2V0aG9tZWFkZHJlc3NcIiwgZnVuY3Rpb24oKSB7XG4gICAgICB2YXIgZWxlbSwgZmssIGhsZGF0YSwgdGhpc190ciwgdmFsdWU7XG4gICAgICB0aGlzX3RyID0gJCh0aGlzKS5jbG9zZXN0KCd0cicpO1xuICAgICAgaGxkYXRhID0gJCgnLmZvcm1lbGVtZW50LWhvbWVfbG9jYXRpb24gaW5wdXQnLCB0aGlzX3RyKS52YWwoKTtcbiAgICAgIGhsZGF0YSA9IEpTT04ucGFyc2UoaGxkYXRhKTtcbiAgICAgIGZvciAoZmsgaW4gaGxkYXRhKSB7XG4gICAgICAgIHZhbHVlID0gaGxkYXRhW2ZrXTtcbiAgICAgICAgaWYgKGZrID09PSAnbG9jYXRpb25fY291bnR5JyB8fCBmayA9PT0gJ2xvY2F0aW9uX3N0YXRlX25hbWUnKSB7XG4gICAgICAgICAgZWxlbSA9ICQoXCIuZm9ybWVsZW1lbnQtXCIgKyBmayArIFwiIHNlbGVjdFwiLCB0aGlzX3RyKTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICBlbGVtID0gJChcIi5mb3JtZWxlbWVudC1cIiArIGZrICsgXCIgaW5wdXRcIiwgdGhpc190cik7XG4gICAgICAgIH1cbiAgICAgICAgaWYgKGVsZW0ubGVuZ3RoID4gMCkge1xuICAgICAgICAgICQoZWxlbSkudmFsKHZhbHVlKS50cmlnZ2VyKCdjaGFuZ2UnKTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgICAgcmV0dXJuIGZhbHNlO1xuICAgIH0pO1xuICB9XG4gIGlmIChmb3JtNDMzYV9wYWdlID09PSAnaXNfcGFnZTZfYWN0aXZlJykge1xuICAgIHN1Z2dlc3Rpb25zID0gJCgnLmlycy1zdWdnZXN0aW9ucy1kYXRhJykuaHRtbCgpO1xuICAgIHN1Z2dlc3Rpb25zID0gSlNPTi5wYXJzZShzdWdnZXN0aW9ucyk7XG4gICAgZm9yIChpID0gMCwgbGVuID0gc3VnZ2VzdGlvbnMubGVuZ3RoOyBpIDwgbGVuOyBpKyspIHtcbiAgICAgIHN1Z2cgPSBzdWdnZXN0aW9uc1tpXTtcbiAgICAgIGVsZW1lbnQgPSAkKHN1Z2dbJ2VsZW1lbnQtc2VsZWN0b3InXSk7XG4gICAgICBkYXRhID0gJzxwIGNsYXNzPVwic3VnZ1wiPjxzcGFuIGNsYXNzPVwiJyArIHN1Z2dbJ2NsYXNzJ10gKyAnXCI+SVJTIEV4cHJlc3Mgc3VnZ2VzdHM6IDxzcGFuIGNsYXNzPVwidmFsdWVcIj4nICsgc3VnZ1sndmFsdWUnXSArICc8L3NwYW4+PC9zcGFuPjxzcGFuIGNsYXNzPVwiZGVzY1wiPicgKyBzdWdnWydkZXNjJ10gKyAnPC9zcGFuPjwvcD4nO1xuICAgICAgJChkYXRhKS5pbnNlcnRBZnRlcihlbGVtZW50KTtcbiAgICB9XG4gICAgd2luZG93LmNhbGNfZXhwZW5zZXMgPSBmdW5jdGlvbigpIHtcbiAgICAgIHZhciBleHBlbnNlLCBpbmNvbWUsIG5ldGRpZmY7XG4gICAgICBpbmNvbWUgPSBleHBlbnNlID0gMDtcbiAgICAgICQoXCIuZm9ybTQzM2EgLmluY29tZV9maWVsZFwiKS5lYWNoKGZ1bmN0aW9uKCkge1xuICAgICAgICB2YXIgaHZhbDtcbiAgICAgICAgaWYgKCQodGhpcykuYXR0cignaWQnKSA9PT0gJ2lkX25ldF9idXNpbmVzc19pbmNvbWUnKSB7XG4gICAgICAgICAgaHZhbCA9ICQodGhpcykuaHRtbCgpLnJlcGxhY2UoL1tcXDxcXD5zcGFuXFxzXFwkXFwvXS9nLCAnJyk7XG4gICAgICAgICAgaW5jb21lICs9IG15cGFyc2VJbnQoaHZhbCk7XG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgaW5jb21lICs9IG15cGFyc2VJbnQoJCh0aGlzKS52YWwoKSk7XG4gICAgICAgIH1cbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICB9KTtcbiAgICAgICQoXCIuZm9ybTQzM2EgLmV4cGVuc2VfZmllbGRcIikuZWFjaChmdW5jdGlvbigpIHtcbiAgICAgICAgZXhwZW5zZSArPSBteXBhcnNlSW50KCQodGhpcykudmFsKCkpO1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH0pO1xuICAgICAgJChcIi5mb3JtNDMzYSAjaWRfdG90YWxfaW5jb21lX2NudCBzcGFuXCIpLmh0bWwoaW5jb21lKS5rZXl1cCgpO1xuICAgICAgJChcIi5mb3JtNDMzYSAjaWRfdG90YWxfZXhwZW5zZXNfY250IHNwYW5cIikuaHRtbChleHBlbnNlKS5rZXl1cCgpO1xuICAgICAgbmV0ZGlmZiA9IGluY29tZSAtIGV4cGVuc2U7XG4gICAgICByZXR1cm4gJChcIi5mb3JtNDMzYSAjaWRfbmV0X2RpZmZlcmVuY2VfY250IHNwYW5cIikuaHRtbChuZXRkaWZmKS5rZXl1cCgpO1xuICAgIH07XG4gICAgJChkb2N1bWVudCkub24oXCJrZXl1cFwiLCBcIi5mb3JtNDMzYSAuaW5wZmxkXCIsIGZ1bmN0aW9uKCkge1xuICAgICAgcmV0dXJuIGNhbGNfZXhwZW5zZXMoKTtcbiAgICB9KTtcbiAgICBjYWxjX2V4cGVuc2VzKCk7XG4gICAgbWFza19udW0oXCIuZm9ybTQzM2EgI2lkX25ldF9idXNpbmVzc19pbmNvbWUgc3BhblwiKTtcbiAgICBtYXNrX251bShcIi5mb3JtNDMzYSAjaWRfdG90YWxfaW5jb21lX2NudCBzcGFuXCIpO1xuICAgIG1hc2tfbnVtKFwiLmZvcm00MzNhICNpZF90b3RhbF9leHBlbnNlc19jbnQgc3BhblwiKTtcbiAgICBtYXNrX251bShcIi5mb3JtNDMzYSAjaWRfbmV0X2RpZmZlcmVuY2VfY250IHNwYW5cIik7XG4gIH1cbiAgaWYgKGZvcm00MzNhX3BhZ2UgPT09ICdpc19wYWdlN19hY3RpdmUnKSB7XG4gICAgd2luZG93LmhpZGVfcGFnZTdfZWxlbWVudHMgPSBmdW5jdGlvbigpIHtcbiAgICAgIHJldHVybiAkKCcuZm9ybTQzM2EtcGFnZS03ID4gdGFibGUgPiB0Ym9keSA+IHRyJykuZWFjaChmdW5jdGlvbigpIHtcbiAgICAgICAgdmFyIHRoaXNfdHI7XG4gICAgICAgIHRoaXNfdHIgPSAkKHRoaXMpO1xuICAgICAgICBpZiAoJCgnaW5wdXRbbmFtZT1cImlzX3NlbGZfZW1wbG95ZWRcIl0nLCB0aGlzX3RyKS5sZW5ndGggPiAwKSB7XG4gICAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICAgIH1cbiAgICAgICAgdGhpc190ci5oaWRlKCk7XG4gICAgICAgIHJldHVybiB0cnVlO1xuICAgICAgfSk7XG4gICAgfTtcbiAgICB3aW5kb3cuc2hvd19wYWdlN19lbGVtZW50cyA9IGZ1bmN0aW9uKCkge1xuICAgICAgJCgnLmZvcm00MzNhLXBhZ2UtNyA+IHRhYmxlID4gdGJvZHkgPiB0cicpLmVhY2goZnVuY3Rpb24oKSB7XG4gICAgICAgIHZhciB0aGlzX3RyO1xuICAgICAgICB0aGlzX3RyID0gJCh0aGlzKTtcbiAgICAgICAgaWYgKCQoJ2lucHV0W25hbWU9XCJpc19zZWxmX2VtcGxveWVkXCJdJywgdGhpc190cikubGVuZ3RoID4gMCkge1xuICAgICAgICAgIHJldHVybiB0cnVlO1xuICAgICAgICB9XG4gICAgICAgIHRoaXNfdHIuc2hvdygpO1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH0pO1xuICAgICAgaWYgKCEkKCcuZm9ybTQzM2EgaW5wdXRbbmFtZT1cImhhc19iYW5rX2FjY291bnRcIl0nKS5kYXRhKFwiYm9vdHN0cmFwLXN3aXRjaFwiKS5zdGF0ZSgpKSB7XG4gICAgICAgICQoJy5zaG93aGlkZXdpdGgtY2hrLWJ1c2luZXNzYmFua2FjYycpLmNsb3Nlc3QoJ3RyLmZpZWxkcm93JykuaGlkZSgpO1xuICAgICAgfVxuICAgICAgaWYgKCEkKCcuZm9ybTQzM2EgaW5wdXRbbmFtZT1cImhhc19hY2NvdW50c19yZWNlaXZhYmxlXCJdJykuZGF0YShcImJvb3RzdHJhcC1zd2l0Y2hcIikuc3RhdGUoKSkge1xuICAgICAgICAkKCcuc2hvd2hpZGV3aXRoLWNoay1hY2NvdW50c3JlY2VpdmFibGUnKS5jbG9zZXN0KCd0ci5maWVsZHJvdycpLmhpZGUoKTtcbiAgICAgIH1cbiAgICAgIGlmICghJCgnLmZvcm00MzNhIGlucHV0W25hbWU9XCJoYXNfYnVzaW5lc3NfYXNzZXRzXCJdJykuZGF0YShcImJvb3RzdHJhcC1zd2l0Y2hcIikuc3RhdGUoKSkge1xuICAgICAgICByZXR1cm4gJCgnLnNob3doaWRld2l0aC1jaGstYnVzaW5lc3Nhc3NldCcpLmNsb3Nlc3QoJ3RyLmZpZWxkcm93JykuaGlkZSgpO1xuICAgICAgfVxuICAgIH07XG4gICAgJCgnLmZvcm00MzNhIGlucHV0W25hbWU9XCJpc19zZWxmX2VtcGxveWVkXCJdJykub24oJ3N3aXRjaENoYW5nZS5ib290c3RyYXBTd2l0Y2gnLCBmdW5jdGlvbihldmVudCwgc3RhdGUpIHtcbiAgICAgIHZhciB0aGlzX3RyO1xuICAgICAgaWYgKHN0YXRlKSB7XG4gICAgICAgIHRoaXNfdHIgPSAkKHRoaXMpLmNsb3Nlc3QoJ3RyJyk7XG4gICAgICAgIHNob3dfcGFnZTdfZWxlbWVudHMoKTtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIGhpZGVfcGFnZTdfZWxlbWVudHMoKTtcbiAgICAgIH1cbiAgICAgIHJldHVybiB0cnVlO1xuICAgIH0pO1xuICAgIGlmICghJCgnLmZvcm00MzNhIGlucHV0W25hbWU9XCJpc19zZWxmX2VtcGxveWVkXCJdJykuZGF0YShcImJvb3RzdHJhcC1zd2l0Y2hcIikuc3RhdGUoKSkge1xuICAgICAgaGlkZV9wYWdlN19lbGVtZW50cygpO1xuICAgIH1cbiAgICAkKGRvY3VtZW50KS5vbihcImtleXVwXCIsIFwiLmZvcm00MzNhIC5iYmFfYWNjb3VudF9iYWxhbmNlXCIsIGZ1bmN0aW9uKCkge1xuICAgICAgdmFyIGNibms7XG4gICAgICBjYm5rID0gMDtcbiAgICAgICQoXCIuZm9ybTQzM2EgLmJiYV9hY2NvdW50X2JhbGFuY2VcIikuZWFjaChmdW5jdGlvbigpIHtcbiAgICAgICAgY2JuayArPSBteXBhcnNlSW50KCQodGhpcykudmFsKCkpO1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH0pO1xuICAgICAgcmV0dXJuICQoXCIuZm9ybTQzM2EgI2lkX3RvdGFsX2Nhc2hfaW5fYmFua3NcIikudmFsKGNibmspLmtleXVwKCk7XG4gICAgfSk7XG4gICAgJChkb2N1bWVudCkub24oXCJrZXl1cFwiLCBcIi5mb3JtNDMzYSAuYXJfYW1vdW50X2R1ZVwiLCBmdW5jdGlvbigpIHtcbiAgICAgIHZhciBhcmFkO1xuICAgICAgYXJhZCA9IDA7XG4gICAgICAkKFwiLmZvcm00MzNhIC5hcl9hbW91bnRfZHVlXCIpLmVhY2goZnVuY3Rpb24oKSB7XG4gICAgICAgIGFyYWQgKz0gbXlwYXJzZUludCgkKHRoaXMpLnZhbCgpKTtcbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICB9KTtcbiAgICAgIHJldHVybiAkKFwiLmZvcm00MzNhICNpZF9vdXRzdGFuZGluZ19iYWxhbmNlXCIpLnZhbChhcmFkKS5rZXl1cCgpO1xuICAgIH0pO1xuICAgICQoZG9jdW1lbnQpLm9uKFwia2V5dXBcIiwgXCIuZm9ybTQzM2EgLmJhZm12X2NsYlwiLCBmdW5jdGlvbigpIHtcbiAgICAgIHZhciBlcXVpdHksIGxiLCBtdjtcbiAgICAgIGxiID0gbXYgPSAwO1xuICAgICAgJChcIi5mb3JtNDMzYSAuYmFjdXJyZW50X2xvYW5fYmFsYW5jZVwiKS5lYWNoKGZ1bmN0aW9uKCkge1xuICAgICAgICBsYiArPSBteXBhcnNlSW50KCQodGhpcykudmFsKCkpO1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH0pO1xuICAgICAgJChcIi5mb3JtNDMzYSAuYmFtYXJrZXRfdmFsdWVcIikuZWFjaChmdW5jdGlvbigpIHtcbiAgICAgICAgbXYgKz0gbXlwYXJzZUludCgkKHRoaXMpLnZhbCgpKTtcbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICB9KTtcbiAgICAgIGVxdWl0eSA9IG12IC0gbGI7XG4gICAgICByZXR1cm4gJChcIi5mb3JtNDMzYSAjaWRfdG90YWxfZXF1aXR5XCIpLnZhbChlcXVpdHkpLmtleXVwKCk7XG4gICAgfSk7XG4gICAgJChkb2N1bWVudCkub24oXCJjbGlja1wiLCBcIi5mb3JtNDMzYSAucGEtc2V0YnVzaW5lc3NhZGRyZXNzXCIsIGZ1bmN0aW9uKCkge1xuICAgICAgdmFyIGJzZWxlbSwgZWxlbSwgaiwgbGVuMSwgbG5hbWUsIGxvY25hbWVzLCB0aGlzX3RyO1xuICAgICAgdGhpc190ciA9ICQodGhpcykuY2xvc2VzdCgndHInKTtcbiAgICAgIGxvY25hbWVzID0gWydzdHJlZXQnLCAnY2l0eScsICdzdGF0ZV9uYW1lJywgJ3ppcGNvZGUnLCAnY291bnR5J107XG4gICAgICBmb3IgKGogPSAwLCBsZW4xID0gbG9jbmFtZXMubGVuZ3RoOyBqIDwgbGVuMTsgaisrKSB7XG4gICAgICAgIGxuYW1lID0gbG9jbmFtZXNbal07XG4gICAgICAgIGlmIChsbmFtZSA9PT0gJ2NvdW50eScgfHwgbG5hbWUgPT09ICdzdGF0ZV9uYW1lJykge1xuICAgICAgICAgIGVsZW0gPSAkKFwiLmZvcm1lbGVtZW50LWxvY2F0aW9uX1wiICsgbG5hbWUgKyBcIiBzZWxlY3RcIiwgdGhpc190cik7XG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgZWxlbSA9ICQoXCIuZm9ybWVsZW1lbnQtbG9jYXRpb25fXCIgKyBsbmFtZSArIFwiIGlucHV0XCIsIHRoaXNfdHIpO1xuICAgICAgICB9XG4gICAgICAgIGJzZWxlbSA9ICQoXCIjaWRfYnVzaW5lc3NfXCIgKyBsbmFtZSk7XG4gICAgICAgIGlmIChlbGVtLmxlbmd0aCA+IDAgJiYgYnNlbGVtLmxlbmd0aCA+IDApIHtcbiAgICAgICAgICBjb25zb2xlLmxvZyhcIlNldCBcIiArIGxuYW1lKTtcbiAgICAgICAgICAkKGVsZW0pLnZhbCgkKGJzZWxlbSkudmFsKCkpLnRyaWdnZXIoJ2NoYW5nZScpO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgIGNvbnNvbGUubG9nKFwiQ2Fubm90IHNldCBcIiArIGxuYW1lKTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgICAgcmV0dXJuIGZhbHNlO1xuICAgIH0pO1xuICB9XG4gIGlmIChmb3JtNDMzYV9wYWdlID09PSAnaXNfcGFnZThfYWN0aXZlJykge1xuICAgIHdpbmRvdy5jYWxjX2V4cGVuc2VzID0gZnVuY3Rpb24oKSB7XG4gICAgICB2YXIgZXhwZW5zZSwgaW5jb21lLCBuZXRkaWZmO1xuICAgICAgaW5jb21lID0gZXhwZW5zZSA9IDA7XG4gICAgICAkKFwiLmZvcm00MzNhIC5pbmNvbWVfZmllbGRcIikuZWFjaChmdW5jdGlvbigpIHtcbiAgICAgICAgaW5jb21lICs9IG15cGFyc2VJbnQoJCh0aGlzKS52YWwoKSk7XG4gICAgICAgIHJldHVybiB0cnVlO1xuICAgICAgfSk7XG4gICAgICAkKFwiLmZvcm00MzNhIC5leHBlbnNlX2ZpZWxkXCIpLmVhY2goZnVuY3Rpb24oKSB7XG4gICAgICAgIGV4cGVuc2UgKz0gbXlwYXJzZUludCgkKHRoaXMpLnZhbCgpKTtcbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICB9KTtcbiAgICAgICQoXCIuZm9ybTQzM2EgI2lkX3RvdGFsX2luY29tZV9jbnQgc3BhblwiKS5odG1sKGluY29tZSkua2V5dXAoKTtcbiAgICAgICQoXCIuZm9ybTQzM2EgI2lkX3RvdGFsX2V4cGVuc2VzX2NudCBzcGFuXCIpLmh0bWwoZXhwZW5zZSkua2V5dXAoKTtcbiAgICAgIG5ldGRpZmYgPSBpbmNvbWUgLSBleHBlbnNlO1xuICAgICAgcmV0dXJuICQoXCIuZm9ybTQzM2EgI2lkX25ldF9kaWZmZXJlbmNlX2NudCBzcGFuXCIpLmh0bWwobmV0ZGlmZikua2V5dXAoKTtcbiAgICB9O1xuICAgICQoZG9jdW1lbnQpLm9uKFwia2V5dXBcIiwgXCIuZm9ybTQzM2EgLmlucGZsZFwiLCBmdW5jdGlvbigpIHtcbiAgICAgIHJldHVybiBjYWxjX2V4cGVuc2VzKCk7XG4gICAgfSk7XG4gICAgbWFza19udW0oXCIuZm9ybTQzM2EgI2lkX3RvdGFsX2luY29tZV9jbnQgc3BhblwiKTtcbiAgICBtYXNrX251bShcIi5mb3JtNDMzYSAjaWRfdG90YWxfZXhwZW5zZXNfY250IHNwYW5cIik7XG4gICAgbWFza19udW0oXCIuZm9ybTQzM2EgI2lkX25ldF9kaWZmZXJlbmNlX2NudCBzcGFuXCIpO1xuICAgIHJldHVybiBjYWxjX2V4cGVuc2VzKCk7XG4gIH1cbn0pO1xuIiwiJ3VzZSBzdHJpY3QnO1xuJChmdW5jdGlvbigpIHtcbiAgdmFyIGZvcm02NTZfcGFnZSwgaSwgaW5pdGlhbF9wYXltZW50LCBqLCBtb250aE5hbWVzLCBvZmZlcl9hbW91bnQsIHBheW1lbnRfdmFsO1xuICBmb3JtNjU2X3BhZ2UgPSAkKCcuNjU2LXBhZ2VhY3RpdmUnKS5kYXRhKCd2YWx1ZScpO1xuICBtb250aE5hbWVzID0gW1wiSmFudWFyeVwiLCBcIkZlYnJ1YXJ5XCIsIFwiTWFyY2hcIiwgXCJBcHJpbFwiLCBcIk1heVwiLCBcIkp1bmVcIiwgXCJKdWx5XCIsIFwiQXVndXN0XCIsIFwiU2VwdGVtYmVyXCIsIFwiT2N0b2JlclwiLCBcIk5vdmVtYmVyXCIsIFwiRGVjZW1iZXJcIl07XG4gIGlmIChmb3JtNjU2X3BhZ2UgPT09ICdpc19wYWdlNV9hY3RpdmUnKSB7XG4gICAgd2luZG93LmY2NTZwYWdlNV9yZWNhbGNfbHVtcHN1bSA9IGZ1bmN0aW9uKCkge1xuICAgICAgdmFyIGFkZGF5LCBhZG1vbnRoLCBhZHllYXIsIGNhbl9wYXksIGNudCwgZGVidCwgZXhwZGF0ZSwgaSwgaW5jb21lLCBpbml0aWFsX3BheW1lbnQsIGosIG1vbnRocywgbm93dGltZSwgb2ZmZXJfYW1vdW50LCBwYXltZW50XzEsIHBheW1lbnRfMiwgcGF5bWVudF8zLCBwYXltZW50XzQsIHBheW1lbnRfNSwgcmVtLCByZW1haW5pbmdfYmFsYW5jZSwgcmVzdWx0cywgdmFsdWU7XG4gICAgICBhZG1vbnRoID0gbXlwYXJzZUludCgkKCcjaWRfYXNzZXNzZWRfZGF0ZV9tb250aCcpLnZhbCgpKSAtIDE7XG4gICAgICBhZGRheSA9IG15cGFyc2VJbnQoJCgnI2lkX2Fzc2Vzc2VkX2RhdGVfZGF5JykudmFsKCkpO1xuICAgICAgYWR5ZWFyID0gbXlwYXJzZUludCgkKCcjaWRfYXNzZXNzZWRfZGF0ZV95ZWFyJykudmFsKCkpO1xuICAgICAgaWYgKGFkbW9udGggPT09IDAgfHwgYWRkYXkgPT09IDAgfHwgYWR5ZWFyID09PSAwKSB7XG4gICAgICAgICQoJyNpZF9zdGF0dXRlX2V4cF9kYXRlJykuaHRtbCgnLScpO1xuICAgICAgICAkKCcjaWRfc3RhdHV0ZV9tb250aHNfYXZhaWwnKS5odG1sKCctJyk7XG4gICAgICAgICQoJyNsdW1wc3VtX2RlY2lzaW9uJykuaHRtbCgncHJvYmFibHkgbWF5IGJlJyk7XG4gICAgICAgICQoJyNpZF9zdWdnZXN0ZWRfYW1vdW50IHNwYW4nKS5odG1sKCcwJykua2V5dXAoKTtcbiAgICAgICAgcmV0dXJuICQoJyNpZF9jYW5fcGF5IHNwYW4nKS5odG1sKFwiMFwiKS5rZXl1cCgpO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgZXhwZGF0ZSA9IG5ldyBEYXRlKGFkeWVhciArIDEwLCBhZG1vbnRoLCBhZGRheSk7XG4gICAgICAgIG5vd3RpbWUgPSBuZXcgRGF0ZSgpO1xuICAgICAgICBtb250aHMgPSAoKGV4cGRhdGUgLSBub3d0aW1lKSAvICgxMDAwICogNjAgKiA2MCAqIDI0ICogMzAuNDQpKS50b0ZpeGVkKCk7XG4gICAgICAgICQoJyNpZF9zdGF0dXRlX2V4cF9kYXRlJykuaHRtbChtb250aE5hbWVzW2FkbW9udGhdICsgXCIvXCIgKyBhZGRheSArIFwiL1wiICsgKGFkeWVhciArIDEwKSk7XG4gICAgICAgICQoJyNpZF9zdGF0dXRlX21vbnRoc19hdmFpbCcpLmh0bWwobW9udGhzICsgXCIgbW9udGhzXCIpO1xuICAgICAgICBpbmNvbWUgPSBteXBhcnNlSW50KCQoJyNpZF9tb250aGx5X2luY29tZScpLnZhbCgpKTtcbiAgICAgICAgZGVidCA9IG15cGFyc2VJbnQoJCgnI2lkX2RlYnRfdG90YWwnKS52YWwoKSk7XG4gICAgICAgIGNhbl9wYXkgPSBtb250aHMgKiBpbmNvbWU7XG4gICAgICAgICQoJyNpZF9jYW5fcGF5IHNwYW4nKS5odG1sKFwiXCIgKyBjYW5fcGF5KS5rZXl1cCgpO1xuICAgICAgICBpZiAoY2FuX3BheSA8IGRlYnQpIHtcbiAgICAgICAgICAkKCcjbHVtcHN1bV9kZWNpc2lvbicpLmh0bWwoJ01BWSBiZScpO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICQoJyNsdW1wc3VtX2RlY2lzaW9uJykuaHRtbCgnTk9UJyk7XG4gICAgICAgIH1cbiAgICAgICAgJCgnI2lkX3N1Z2dlc3RlZF9hbW91bnQgc3BhbicpLmh0bWwoXCJcIiArIChpbmNvbWUgKiAxMikpLmtleXVwKCk7XG4gICAgICAgIG9mZmVyX2Ftb3VudCA9IG15cGFyc2VJbnQoJCgnI2lkX29mZmVyX2Ftb3VudF9sdW1wc3VtJykudmFsKCkpO1xuICAgICAgICBpbml0aWFsX3BheW1lbnQgPSBteXBhcnNlSW50KCQoJyNpZF9pbml0aWFsX3BheW1lbnQnKS52YWwoKSk7XG4gICAgICAgIHBheW1lbnRfMSA9IG15cGFyc2VJbnQoJCgnI2lkX3BheW1lbnRfMScpLnZhbCgpKTtcbiAgICAgICAgcGF5bWVudF8yID0gbXlwYXJzZUludCgkKCcjaWRfcGF5bWVudF8yJykudmFsKCkpO1xuICAgICAgICBwYXltZW50XzMgPSBteXBhcnNlSW50KCQoJyNpZF9wYXltZW50XzMnKS52YWwoKSk7XG4gICAgICAgIHBheW1lbnRfNCA9IG15cGFyc2VJbnQoJCgnI2lkX3BheW1lbnRfNCcpLnZhbCgpKTtcbiAgICAgICAgcGF5bWVudF81ID0gbXlwYXJzZUludCgkKCcjaWRfcGF5bWVudF81JykudmFsKCkpO1xuICAgICAgICBpZiAob2ZmZXJfYW1vdW50ID09PSAwIHx8ICF3aW5kb3cub2ZmZXJfYW1vdW50X2NoYW5nZWQpIHtcbiAgICAgICAgICBvZmZlcl9hbW91bnQgPSBpbmNvbWUgKiAxMjtcbiAgICAgICAgICAkKCcjaWRfb2ZmZXJfYW1vdW50X2x1bXBzdW0nKS52YWwob2ZmZXJfYW1vdW50KS5rZXl1cCgpO1xuICAgICAgICAgIG1hcmtfdW5zYXZlZCgpO1xuICAgICAgICB9XG4gICAgICAgIGlmIChpbml0aWFsX3BheW1lbnQgPT09IDAgfHwgIXdpbmRvdy5pbml0aWFsX3BheW1lbnRfY2hhbmdlZCkge1xuICAgICAgICAgIGluaXRpYWxfcGF5bWVudCA9IChvZmZlcl9hbW91bnQgLyA1KS50b0ZpeGVkKCk7XG4gICAgICAgICAgJCgnI2lkX2luaXRpYWxfcGF5bWVudCcpLnZhbChpbml0aWFsX3BheW1lbnQpLmtleXVwKCk7XG4gICAgICAgICAgbWFya191bnNhdmVkKCk7XG4gICAgICAgIH1cbiAgICAgICAgcmVtYWluaW5nX2JhbGFuY2UgPSBvZmZlcl9hbW91bnQgLSBpbml0aWFsX3BheW1lbnQ7XG4gICAgICAgICQoJyNpZF9yZW1haW5pbmdfYmFsYW5jZSBzcGFuJykuaHRtbChyZW1haW5pbmdfYmFsYW5jZSkua2V5dXAoKTtcbiAgICAgICAgcmVtID0gcmVtYWluaW5nX2JhbGFuY2U7XG4gICAgICAgIGNudCA9IDY7XG4gICAgICAgIHJlc3VsdHMgPSBbXTtcbiAgICAgICAgZm9yIChpID0gaiA9IDE7IGogPD0gNTsgaSA9ICsraikge1xuICAgICAgICAgIHZhbHVlID0gKHJlbSAvIChjbnQgLSBpKSkudG9GaXhlZCgpO1xuICAgICAgICAgIHJlbSA9IHJlbSAtIHZhbHVlO1xuICAgICAgICAgICQoXCIjcGF5bWVudF9cIiArIGkgKyBcIl9hZHZpY2Ugc3Bhbi5maWVsZC1udW1iZXJcIikuaHRtbCh2YWx1ZSkua2V5dXAoKTtcbiAgICAgICAgICBpZiAoIXdpbmRvdy5wYXltZW50c19jaGFuZ2VkW2ldKSB7XG4gICAgICAgICAgICByZXN1bHRzLnB1c2goJChcIiNpZF9wYXltZW50X1wiICsgaSkudmFsKHZhbHVlKS5rZXl1cCgpKTtcbiAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgcmVzdWx0cy5wdXNoKHZvaWQgMCk7XG4gICAgICAgICAgfVxuICAgICAgICB9XG4gICAgICAgIHJldHVybiByZXN1bHRzO1xuICAgICAgfVxuICAgIH07XG4gICAgb2ZmZXJfYW1vdW50ID0gbXlwYXJzZUludCgkKCcjaWRfb2ZmZXJfYW1vdW50X2x1bXBzdW0nKS52YWwoKSk7XG4gICAgaW5pdGlhbF9wYXltZW50ID0gbXlwYXJzZUludCgkKCcjaWRfaW5pdGlhbF9wYXltZW50JykudmFsKCkpO1xuICAgIHdpbmRvdy5vZmZlcl9hbW91bnRfY2hhbmdlZCA9IG9mZmVyX2Ftb3VudCA+IDA7XG4gICAgd2luZG93LmluaXRpYWxfcGF5bWVudF9jaGFuZ2VkID0gaW5pdGlhbF9wYXltZW50ID4gMDtcbiAgICB3aW5kb3cucGF5bWVudHNfY2hhbmdlZCA9IFtmYWxzZSwgZmFsc2UsIGZhbHNlLCBmYWxzZSwgZmFsc2VdO1xuICAgIGZvciAoaSA9IGogPSAxOyBqIDw9IDU7IGkgPSArK2opIHtcbiAgICAgIHBheW1lbnRfdmFsID0gbXlwYXJzZUludCgkKFwiI2lkX3BheW1lbnRfXCIgKyBpKS52YWwoKSk7XG4gICAgICB3aW5kb3cucGF5bWVudHNfY2hhbmdlZFtpXSA9IHBheW1lbnRfdmFsID4gMDtcbiAgICAgICQoXCIjaWRfcGF5bWVudF9cIiArIGkpLmNzcygnd2lkdGgnLCAyMDApLmNzcygnZGlzcGxheScsICdpbmxpbmUnKTtcbiAgICAgICQoJzxzcGFuIGlkPVwicGF5bWVudF8nICsgaSArICdfYWR2aWNlXCIgZGF0YS1waT1cIicgKyBpICsgJ1wiIGNsYXNzPVwicGF5bWVudF9hZHZpY2VcIj48c3BhbiBjbGFzcz1cImZhIGZhLWFycm93LWxlZnRcIj48L3NwYW4+ICQgPHNwYW4gY2xhc3M9XCJmaWVsZC1udW1iZXJcIj4wPC9zcGFuPjwvc3Bhbj4nKS5pbnNlcnRBZnRlcihcIiNpZF9wYXltZW50X1wiICsgaSk7XG4gICAgfVxuICAgICQoZG9jdW1lbnQpLm9uKCdjbGljaycsICcucGF5bWVudF9hZHZpY2UnLCBmdW5jdGlvbigpIHtcbiAgICAgIHZhciBwaSwgdGhpc3RyLCB2O1xuICAgICAgdiA9ICQoJ3NwYW4uZmllbGQtbnVtYmVyJywgdGhpcykuaHRtbCgpO1xuICAgICAgdGhpc3RyID0gJCh0aGlzKS5jbG9zZXN0KCd0cicpO1xuICAgICAgJCgnaW5wdXQnLCB0aGlzdHIpLnZhbCh2KS5rZXl1cCgpO1xuICAgICAgcGkgPSAkKHRoaXMpLmRhdGEoJ3BpJyk7XG4gICAgICByZXR1cm4gd2luZG93LnBheW1lbnRzX2NoYW5nZWRbcGldID0gZmFsc2U7XG4gICAgfSk7XG4gICAgZjY1NnBhZ2U1X3JlY2FsY19sdW1wc3VtKCk7XG4gICAgJCgnLmZvcm1lbGVtZW50LWFzc2Vzc2VkX2RhdGUnKS5vbignY2hhbmdlJywgJ3NlbGVjdCcsIGZ1bmN0aW9uKCkge1xuICAgICAgcmV0dXJuIGY2NTZwYWdlNV9yZWNhbGNfbHVtcHN1bSgpO1xuICAgIH0pO1xuICAgICQoJyNpZF9tb250aGx5X2luY29tZScpLm9uKCdjaGFuZ2UnLCBmdW5jdGlvbigpIHtcbiAgICAgIHJldHVybiBmNjU2cGFnZTVfcmVjYWxjX2x1bXBzdW0oKTtcbiAgICB9KTtcbiAgICAkKCcjaWRfZGVidF90b3RhbCcpLm9uKCdjaGFuZ2UnLCBmdW5jdGlvbigpIHtcbiAgICAgIHJldHVybiBmNjU2cGFnZTVfcmVjYWxjX2x1bXBzdW0oKTtcbiAgICB9KTtcbiAgICAkKCcjaWRfb2ZmZXJfYW1vdW50X2x1bXBzdW0nKS5vbignY2hhbmdlJywgZnVuY3Rpb24oKSB7XG4gICAgICB3aW5kb3cub2ZmZXJfYW1vdW50X2NoYW5nZWQgPSB0cnVlO1xuICAgICAgcmV0dXJuIGY2NTZwYWdlNV9yZWNhbGNfbHVtcHN1bSgpO1xuICAgIH0pO1xuICAgIHJldHVybiAkKCcjaWRfaW5pdGlhbF9wYXltZW50Jykub24oJ2NoYW5nZScsIGZ1bmN0aW9uKCkge1xuICAgICAgd2luZG93LmluaXRpYWxfcGF5bWVudF9jaGFuZ2VkID0gdHJ1ZTtcbiAgICAgIHJldHVybiBmNjU2cGFnZTVfcmVjYWxjX2x1bXBzdW0oKTtcbiAgICB9KTtcbiAgfVxufSk7XG4iLCIndXNlIHN0cmljdCc7XG4kKGZ1bmN0aW9uKCkge1xuICB2YXIgZm9ybWlkO1xuICBpZiAoJCgnZm9ybSNwYWdlZm9ybSAuaXJzZm9ybScpLmxlbmd0aCA+IDApIHtcbiAgICB3aW5kb3cuZGlzYWJsZV9zd2l0Y2ggPSBmYWxzZTtcbiAgICB3aW5kb3cuc2hvd18xeDFfc3ViZm9ybSA9IGZ1bmN0aW9uKHByZXYsIHNyY191cmwsIHVubG9ja19uYW1lKSB7XG4gICAgICBpZiAoIXNyY191cmwpIHtcbiAgICAgICAgY29uc29sZS5leGNlcHRpb24oXCIxeDEgc3ViZm9ybTogc3JjX3VybCBpcyBlbXB0eSFcIik7XG4gICAgICAgIHJldHVybiBmYWxzZTtcbiAgICAgIH1cbiAgICAgIHJldHVybiAkLmFqYXgoc3JjX3VybCwge1xuICAgICAgICB0eXBlOiAnR0VUJyxcbiAgICAgICAgZGF0YVR5cGU6ICdodG1sJyxcbiAgICAgICAgc3VjY2VzczogZnVuY3Rpb24oZGF0YSwgdGV4dFN0YXR1cywganFYSFIpIHtcbiAgICAgICAgICAkKGRhdGEpLmluc2VydEFmdGVyKHByZXYpO1xuICAgICAgICAgIHJlaW5pdFdpZGdldHMoKTtcbiAgICAgICAgICBpZiAodW5sb2NrX25hbWUpIHtcbiAgICAgICAgICAgIGNvbnRlbnRfbG9hZGVkKHVubG9ja19uYW1lKTtcbiAgICAgICAgICB9XG4gICAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgICAgICB9XG4gICAgICB9KTtcbiAgICB9O1xuICAgICQoJy5pcnNmb3JtIGlucHV0LmZvcm0xeDFzd2l0Y2hlcicpLm9uKCdzd2l0Y2hDaGFuZ2UuYm9vdHN0cmFwU3dpdGNoJywgZnVuY3Rpb24oZXZlbnQsIHN0YXRlKSB7XG4gICAgICB2YXIgc3JjX3VybCwgc3ViZm9ybV9zZWxlY3Rvciwgc3ViZm9ybW5hbWUsIHRoaXNfdHI7XG4gICAgICBpZiAod2luZG93LmRpc2FibGVfc3dpdGNoKSB7XG4gICAgICAgIHJldHVybiB0cnVlO1xuICAgICAgfVxuICAgICAgd2luZG93LmRpc2FibGVfc3dpdGNoID0gdHJ1ZTtcbiAgICAgIHN1YmZvcm1uYW1lID0gJCh0aGlzKS5kYXRhKCdzdWJmb3JtLW5hbWUnKTtcbiAgICAgIHNyY191cmwgPSAkKFwiI1wiICsgc3ViZm9ybW5hbWUgKyBcIl9mb3JtX3VybFwiKS5kYXRhKCd1cmwnKTtcbiAgICAgIHN1YmZvcm1fc2VsZWN0b3IgPSAkKFwiI1wiICsgc3ViZm9ybW5hbWUgKyBcIl9mb3JtX3VybFwiKS5kYXRhKCdzdWJmb3JtLXNlbGVjdG9yJyk7XG4gICAgICBpZiAoc3RhdGUpIHtcbiAgICAgICAgdGhpc190ciA9ICQodGhpcykuY2xvc2VzdCgndHInKTtcbiAgICAgICAgc2hvd18xeDFfc3ViZm9ybSh0aGlzX3RyLCBzcmNfdXJsKTtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIGlmICghY29uZmlybShcIlRoaXMgYWN0aW9uIHdpbGwgcmVtb3ZlIHRoZSBzZWN0aW9uIGJlbG93LiBBcmUgeW91IHN1cmU/XCIpKSB7XG4gICAgICAgICAgd2luZG93LmRpc2FibGVfc3dpdGNoID0gdHJ1ZTtcbiAgICAgICAgICAkKHRoaXMpLmRhdGEoXCJib290c3RyYXAtc3dpdGNoXCIpLnN0YXRlKHRydWUpO1xuICAgICAgICAgIHdpbmRvdy5kaXNhYmxlX3N3aXRjaCA9IGZhbHNlO1xuICAgICAgICAgIHJldHVybiB0cnVlO1xuICAgICAgICB9XG4gICAgICAgICQodGhpcykuZGF0YShcImJvb3RzdHJhcC1zd2l0Y2hcIikuc3RhdGUoZmFsc2UpO1xuICAgICAgICAkKHN1YmZvcm1fc2VsZWN0b3IpLnJlbW92ZSgpO1xuICAgICAgfVxuICAgICAgd2luZG93LmRpc2FibGVfc3dpdGNoID0gZmFsc2U7XG4gICAgICByZXR1cm4gdHJ1ZTtcbiAgICB9KTtcbiAgICBpZiAoJCgnLmlyc2Zvcm0gaW5wdXQuZm9ybTF4MXN3aXRjaGVyJykubGVuZ3RoID4gMCkge1xuICAgICAgJCgnLmlyc2Zvcm0gaW5wdXQuZm9ybTF4MXN3aXRjaGVyJykuZWFjaChmdW5jdGlvbigpIHtcbiAgICAgICAgdmFyIHNyY191cmwsIHN1YmZvcm1uYW1lLCB0aGlzX3RyO1xuICAgICAgICBzdWJmb3JtbmFtZSA9ICQodGhpcykuZGF0YSgnc3ViZm9ybS1uYW1lJyk7XG4gICAgICAgIHNyY191cmwgPSAkKFwiI1wiICsgc3ViZm9ybW5hbWUgKyBcIl9mb3JtX3VybFwiKS5kYXRhKCd1cmwnKTtcbiAgICAgICAgaWYgKCQodGhpcykuZGF0YShcImJvb3RzdHJhcC1zd2l0Y2hcIikuc3RhdGUoKSkge1xuICAgICAgICAgIHdhaXRsb2FkX2xpc3Rbc3ViZm9ybW5hbWVdID0gdHJ1ZTtcbiAgICAgICAgICB0aGlzX3RyID0gJCh0aGlzKS5jbG9zZXN0KCd0cicpO1xuICAgICAgICAgIHNob3dfMXgxX3N1YmZvcm0odGhpc190ciwgc3JjX3VybCwgc3ViZm9ybW5hbWUpO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiB0cnVlO1xuICAgICAgfSk7XG4gICAgfVxuICAgIHdpbmRvdy5hZGp1c3RfY2FsY3VsYXRpb25zID0gZnVuY3Rpb24oKSB7XG4gICAgICAkKCcuZm9ybTQzM2EtcGFnZS00IGlucHV0Lm51bWJlci1maWVsZCcpLmtleXVwKCk7XG4gICAgICAkKCcuZm9ybTQzM2EtcGFnZS01IGlucHV0Lm51bWJlci1maWVsZCcpLmtleXVwKCk7XG4gICAgICByZXR1cm4gJCgnLmZvcm00MzNhLXBhZ2UtNyBpbnB1dC5udW1iZXItZmllbGQnKS5rZXl1cCgpO1xuICAgIH07XG4gICAgd2luZG93LnN1YmZvcm1zXzF4bl9jb3VudHMgPSB7fTtcbiAgICB3aW5kb3cuc3ViZm9ybXNfMXhuX21heGNvdW50cyA9IHt9O1xuICAgIHdpbmRvdy5hZGRfMXhuX3N1YmZvcm0gPSBmdW5jdGlvbihwcmV2LCBzcmNfdXJsLCBzdWJmb3JtbmFtZSwgdW5sb2NrX25hbWUpIHtcbiAgICAgIHZhciBjbnQsIG1heGNudDtcbiAgICAgIGlmICghc3JjX3VybCkge1xuICAgICAgICBjb25zb2xlLmV4Y2VwdGlvbihcIjF4biBzdWJmb3JtOiBzcmNfdXJsIGlzIGVtcHR5IVwiKTtcbiAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgICAgfVxuICAgICAgbWF4Y250ID0gd2luZG93LnN1YmZvcm1zXzF4bl9tYXhjb3VudHNbc3ViZm9ybW5hbWVdO1xuICAgICAgY250ID0gd2luZG93LnN1YmZvcm1zXzF4bl9jb3VudHNbc3ViZm9ybW5hbWVdO1xuICAgICAgaWYgKG1heGNudCA+IDAgJiYgY250ID09PSBtYXhjbnQpIHtcbiAgICAgICAgYWxlcnQoXCJBbGxvd2VkIG9ubHkgXCIgKyBtYXhjbnQgKyBcIiBpdGVtc1wiKTtcbiAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgICAgfVxuICAgICAgc3JjX3VybCA9ICQoXCIjXCIgKyBzdWJmb3JtbmFtZSArIFwiX2Zvcm1fdXJsXCIpLmRhdGEoJ3VybCcpO1xuICAgICAgd2luZG93LnN1YmZvcm1zXzF4bl9jb3VudHNbc3ViZm9ybW5hbWVdICs9IDE7XG4gICAgICBjbnQgPSB3aW5kb3cuc3ViZm9ybXNfMXhuX2NvdW50c1tzdWJmb3JtbmFtZV07XG4gICAgICAkLmFqYXgoXCJcIiArIHNyY191cmwgKyBzdWJmb3JtbmFtZSArIFwiX1wiICsgY250LCB7XG4gICAgICAgIHR5cGU6ICdHRVQnLFxuICAgICAgICBkYXRhVHlwZTogJ2h0bWwnLFxuICAgICAgICBzdWNjZXNzOiBmdW5jdGlvbihkYXRhLCB0ZXh0U3RhdHVzLCBqcVhIUikge1xuICAgICAgICAgICQoZGF0YSkuaW5zZXJ0QWZ0ZXIocHJldik7XG4gICAgICAgICAgcmVpbml0V2lkZ2V0cygpO1xuICAgICAgICAgIGFkanVzdF9jYWxjdWxhdGlvbnMoKTtcbiAgICAgICAgICBpZiAodW5sb2NrX25hbWUpIHtcbiAgICAgICAgICAgIHJldHVybiBjb250ZW50X2xvYWRlZCh1bmxvY2tfbmFtZSk7XG4gICAgICAgICAgfVxuICAgICAgICB9XG4gICAgICB9KTtcbiAgICAgIHJldHVybiBmYWxzZTtcbiAgICB9O1xuICAgIHdpbmRvdy50b2dnbGUxeE5mb3Jtc2V0ID0gZnVuY3Rpb24oZWxlbWVudCwgbWFuYWdlZCkge1xuICAgICAgdmFyIGRzc2UsIHNlbGVjdG9yLCBzcmNfdXJsLCBzdGF0ZSwgc3ViZm9ybW5hbWUsIHRoaXNfdHI7XG4gICAgICBzdWJmb3JtbmFtZSA9ICQoZWxlbWVudCkuZGF0YSgnc3ViZm9ybS1uYW1lJyk7XG4gICAgICBzdGF0ZSA9ICQoZWxlbWVudCkuZGF0YShcImJvb3RzdHJhcC1zd2l0Y2hcIikuc3RhdGUoKTtcbiAgICAgIGlmIChzdGF0ZSkge1xuICAgICAgICB0aGlzX3RyID0gJChlbGVtZW50KS5jbG9zZXN0KCd0cicpO1xuICAgICAgICB3aW5kb3cuc3ViZm9ybXNfMXhuX2NvdW50c1tzdWJmb3JtbmFtZV0gPSAwO1xuICAgICAgICBzcmNfdXJsID0gJChcIiNcIiArIHN1YmZvcm1uYW1lICsgXCJfZm9ybV91cmxcIikuZGF0YSgndXJsJyk7XG4gICAgICAgIGFkZF8xeG5fc3ViZm9ybSh0aGlzX3RyLCBzcmNfdXJsLCBzdWJmb3JtbmFtZSk7XG4gICAgICAgICQoJy5zaG93aGlkZXdpdGgtY2hrLScgKyBzdWJmb3JtbmFtZSkuY2xvc2VzdCgndHIuZmllbGRyb3cnKS5zaG93KCk7XG4gICAgICB9IGVsc2Uge1xuICAgICAgICBpZiAobWFuYWdlZCkge1xuICAgICAgICAgIGlmICghY29uZmlybShcIlRoaXMgYWN0aW9uIHdpbGwgcmVtb3ZlIHRoZSBzZWN0aW9uIGJlbG93LiBBcmUgeW91IHN1cmU/XCIpKSB7XG4gICAgICAgICAgICB3aW5kb3cuZGlzYWJsZV9zd2l0Y2ggPSB0cnVlO1xuICAgICAgICAgICAgJChlbGVtZW50KS5kYXRhKFwiYm9vdHN0cmFwLXN3aXRjaFwiKS5zdGF0ZSh0cnVlKTtcbiAgICAgICAgICAgIHdpbmRvdy5kaXNhYmxlX3N3aXRjaCA9IGZhbHNlO1xuICAgICAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgICAgICBkc3NlID0gd2luZG93LmRpc2FibGVfc3dpdGNoO1xuICAgICAgICB3aW5kb3cuZGlzYWJsZV9zd2l0Y2ggPSB0cnVlO1xuICAgICAgICAkKGVsZW1lbnQpLmRhdGEoXCJib290c3RyYXAtc3dpdGNoXCIpLnN0YXRlKGZhbHNlKTtcbiAgICAgICAgd2luZG93LmRpc2FibGVfc3dpdGNoID0gZHNzZTtcbiAgICAgICAgc2VsZWN0b3IgPSAkKFwiI1wiICsgc3ViZm9ybW5hbWUgKyBcIl9mb3JtX3VybFwiKS5kYXRhKCdzdWJmb3JtLXNlbGVjdG9yJyk7XG4gICAgICAgICQoc2VsZWN0b3IpLnJlbW92ZSgpO1xuICAgICAgICB3aW5kb3cuc3ViZm9ybXNfMXhuX2NvdW50c1tzdWJmb3JtbmFtZV0gPSAwO1xuICAgICAgICAkKCcuc2hvd2hpZGV3aXRoLWNoay0nICsgc3ViZm9ybW5hbWUpLmNsb3Nlc3QoJ3RyLmZpZWxkcm93JykuaGlkZSgpO1xuICAgICAgfVxuICAgICAgcmV0dXJuIHRydWU7XG4gICAgfTtcbiAgICAkKCcuaXJzZm9ybSBpbnB1dC5mb3JtMXhuc3dpdGNoZXInKS5vbignc3dpdGNoQ2hhbmdlLmJvb3RzdHJhcFN3aXRjaCcsIGZ1bmN0aW9uKGV2ZW50LCBzdGF0ZSkge1xuICAgICAgaWYgKHdpbmRvdy5kaXNhYmxlX3N3aXRjaCkge1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH1cbiAgICAgIHdpbmRvdy5kaXNhYmxlX3N3aXRjaCA9IHRydWU7XG4gICAgICB0b2dnbGUxeE5mb3Jtc2V0KCQodGhpcyksIHRydWUpO1xuICAgICAgd2luZG93LmRpc2FibGVfc3dpdGNoID0gZmFsc2U7XG4gICAgICByZXR1cm4gdHJ1ZTtcbiAgICB9KTtcbiAgICAkKCdmb3JtI3BhZ2Vmb3JtJykub24oXCJjbGlja1wiLCBcIi5hZGQtc3ViZm9ybVwiLCBmdW5jdGlvbigpIHtcbiAgICAgIHZhciBzcmNfdXJsLCBzdWJmb3JtY2xhc3NuYW1lLCBzdWJmb3JtbmFtZSwgdGhpc190cjtcbiAgICAgIHRoaXNfdHIgPSAkKHRoaXMpLmNsb3Nlc3QoJ3RyJyk7XG4gICAgICBzdWJmb3JtY2xhc3NuYW1lID0gJCh0aGlzX3RyKS5kYXRhKCdzdWJmb3JtLWNsYXNzbmFtZScpO1xuICAgICAgc3ViZm9ybW5hbWUgPSAkKCcqW2RhdGEtc3ViZm9ybS1zZWxlY3Rvcj1cIi4nICsgc3ViZm9ybWNsYXNzbmFtZSArICdcIl0nKS5kYXRhKCdzdWJmb3JtLW5hbWUnKTtcbiAgICAgIHNyY191cmwgPSAkKFwiI1wiICsgc3ViZm9ybW5hbWUgKyBcIl9mb3JtX3VybFwiKS5kYXRhKCd1cmwnKTtcbiAgICAgIGFkZF8xeG5fc3ViZm9ybSh0aGlzX3RyLCBzcmNfdXJsLCBzdWJmb3JtbmFtZSk7XG4gICAgICByZXR1cm4gZmFsc2U7XG4gICAgfSk7XG4gICAgJCgnZm9ybSNwYWdlZm9ybScpLm9uKFwiY2xpY2tcIiwgXCIucmVtb3ZlLXN1YmZvcm1cIiwgZnVuY3Rpb24oKSB7XG4gICAgICB2YXIgc3ViZm9ybWNsYXNzbmFtZSwgc3ViZm9ybW5hbWUsIHN3aXRjaGVyLCB0aGlzX3RyO1xuICAgICAgdGhpc190ciA9ICQodGhpcykuY2xvc2VzdCgndHInKTtcbiAgICAgIHN1YmZvcm1jbGFzc25hbWUgPSAkKHRoaXNfdHIpLmRhdGEoJ3N1YmZvcm0tY2xhc3NuYW1lJyk7XG4gICAgICBzdWJmb3JtbmFtZSA9ICQoJypbZGF0YS1zdWJmb3JtLXNlbGVjdG9yPVwiLicgKyBzdWJmb3JtY2xhc3NuYW1lICsgJ1wiXScpLmRhdGEoJ3N1YmZvcm0tbmFtZScpO1xuICAgICAgJCh0aGlzX3RyKS5yZW1vdmUoKTtcbiAgICAgIGFkanVzdF9jYWxjdWxhdGlvbnMoKTtcbiAgICAgIGlmICgkKFwiLlwiICsgc3ViZm9ybWNsYXNzbmFtZSkubGVuZ3RoID09PSAwKSB7XG4gICAgICAgIHdpbmRvdy5kaXNhYmxlX3N3aXRjaCA9IHRydWU7XG4gICAgICAgIHN3aXRjaGVyID0gJChcIi5pcnNmb3JtIGlucHV0LmZvcm0xeG5zd2l0Y2hlci5zd2l0Y2hlci1cIiArIHN1YmZvcm1uYW1lKTtcbiAgICAgICAgc3dpdGNoZXIuZGF0YShcImJvb3RzdHJhcC1zd2l0Y2hcIikuc3RhdGUoZmFsc2UpO1xuICAgICAgICB0b2dnbGUxeE5mb3Jtc2V0KHN3aXRjaGVyLCBmYWxzZSk7XG4gICAgICAgIHdpbmRvdy5kaXNhYmxlX3N3aXRjaCA9IGZhbHNlO1xuICAgICAgICAkKCcuc2hvd2hpZGV3aXRoLWNoay0nICsgc3ViZm9ybW5hbWUpLmNsb3Nlc3QoJ3RyLmZpZWxkcm93JykuaGlkZSgpO1xuICAgICAgfVxuICAgICAgcmV0dXJuIGZhbHNlO1xuICAgIH0pO1xuICAgIGlmICgkKCcuaXJzZm9ybSBpbnB1dC5mb3JtMXhuc3dpdGNoZXInKS5sZW5ndGggPiAwKSB7XG4gICAgICAkKCcuaXJzZm9ybSBpbnB1dC5mb3JtMXhuc3dpdGNoZXInKS5lYWNoKGZ1bmN0aW9uKCkge1xuICAgICAgICB2YXIgaSwgcmVmLCBzcmNfdXJsLCBzdWJmb3JtX2NudCwgc3ViZm9ybV9tYXhjbnQsIHN1YmZvcm1uYW1lLCB0aGlzX3RyLCB4O1xuICAgICAgICBzdWJmb3JtbmFtZSA9ICQodGhpcykuZGF0YSgnc3ViZm9ybS1uYW1lJyk7XG4gICAgICAgIHN1YmZvcm1fY250ID0gJCh0aGlzKS5kYXRhKCdzdWJmb3JtLWNvdW50Jyk7XG4gICAgICAgIHN1YmZvcm1fbWF4Y250ID0gJCh0aGlzKS5kYXRhKCdzdWJmb3JtLW1heGNvdW50Jyk7XG4gICAgICAgIHdpbmRvdy5zdWJmb3Jtc18xeG5fY291bnRzW3N1YmZvcm1uYW1lXSA9IDA7XG4gICAgICAgIHdpbmRvdy5zdWJmb3Jtc18xeG5fbWF4Y291bnRzW3N1YmZvcm1uYW1lXSA9IHN1YmZvcm1fbWF4Y250O1xuICAgICAgICBpZiAoc3ViZm9ybV9jbnQgPiAwKSB7XG4gICAgICAgICAgc3JjX3VybCA9ICQoXCIjXCIgKyBzdWJmb3JtbmFtZSArIFwiX2Zvcm1fdXJsXCIpLmRhdGEoJ3VybCcpO1xuICAgICAgICAgIHRoaXNfdHIgPSAkKHRoaXMpLmNsb3Nlc3QoJ3RyJyk7XG4gICAgICAgICAgJCh0aGlzKS5kYXRhKFwiYm9vdHN0cmFwLXN3aXRjaFwiKS5zdGF0ZSh0cnVlKTtcbiAgICAgICAgICBmb3IgKHggPSBpID0gMSwgcmVmID0gc3ViZm9ybV9jbnQ7IDEgPD0gcmVmID8gaSA8IHJlZiA6IGkgPiByZWY7IHggPSAxIDw9IHJlZiA/ICsraSA6IC0taSkge1xuICAgICAgICAgICAgd2FpdGxvYWRfbGlzdFtzdWJmb3JtbmFtZSArIFwiX1wiICsgeF0gPSB0cnVlO1xuICAgICAgICAgICAgYWRkXzF4bl9zdWJmb3JtKHRoaXNfdHIsIHNyY191cmwsIHN1YmZvcm1uYW1lLCBzdWJmb3JtbmFtZSArIFwiX1wiICsgeCk7XG4gICAgICAgICAgfVxuICAgICAgICAgICQoJy5zaG93aGlkZXdpdGgtY2hrLScgKyBzdWJmb3JtbmFtZSkuY2xvc2VzdCgndHIuZmllbGRyb3cnKS5zaG93KCk7XG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgJCgnLnNob3doaWRld2l0aC1jaGstJyArIHN1YmZvcm1uYW1lKS5jbG9zZXN0KCd0ci5maWVsZHJvdycpLmhpZGUoKTtcbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH0pO1xuICAgIH1cbiAgICAkKGRvY3VtZW50KS5vbignc3dpdGNoQ2hhbmdlLmJvb3RzdHJhcFN3aXRjaCcsICcuY2hrLXJhZGlvZ3JvdXAnLCBmdW5jdGlvbihldmVudCwgc3RhdGUpIHtcbiAgICAgIHZhciBkZXB0ciwgZGVwdHJzLCBpLCBsZW4sIHJlc3VsdHMsIHRyZWxlbTtcbiAgICAgIGRlcHRycyA9ICQodGhpcykuZGF0YSgnZGVwX3Jvd3MnKS5zcGxpdCgnICcpO1xuICAgICAgcmVzdWx0cyA9IFtdO1xuICAgICAgZm9yIChpID0gMCwgbGVuID0gZGVwdHJzLmxlbmd0aDsgaSA8IGxlbjsgaSsrKSB7XG4gICAgICAgIGRlcHRyID0gZGVwdHJzW2ldO1xuICAgICAgICB0cmVsZW0gPSAkKFwiLmZvcm1lbGVtZW50LVwiICsgZGVwdHIpLmNsb3Nlc3QoJ3RyJyk7XG4gICAgICAgIGlmIChzdGF0ZSkge1xuICAgICAgICAgIHRyZWxlbS5yZW1vdmVDbGFzcygnaGlkZGVuJyk7XG4gICAgICAgICAgcmVzdWx0cy5wdXNoKCQoXCIjaWRfXCIgKyBkZXB0cikucmVtb3ZlQ2xhc3MoJ2hpZGRlbicpKTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICBpZiAoIXRyZWxlbS5oYXNDbGFzcygnaGlkZGVuJykpIHtcbiAgICAgICAgICAgIHJlc3VsdHMucHVzaCh0cmVsZW0uYWRkQ2xhc3MoJ2hpZGRlbicpKTtcbiAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgcmVzdWx0cy5wdXNoKHZvaWQgMCk7XG4gICAgICAgICAgfVxuICAgICAgICB9XG4gICAgICB9XG4gICAgICByZXR1cm4gcmVzdWx0cztcbiAgICB9KTtcbiAgICBpZiAoJCgnLnRvZ2dsZS1jaGtib3guZGlzYWJsZWQnKS5sZW5ndGggPiAwKSB7XG4gICAgICAkKCcudG9nZ2xlLWNoa2JveC5kaXNhYmxlZCcpLmRhdGEoXCJib290c3RyYXAtc3dpdGNoXCIpLmRpc2FibGVkKHRydWUpO1xuICAgIH1cbiAgICB3aW5kb3cubWFya191bnNhdmVkID0gZnVuY3Rpb24oZWxlbWVudCkge1xuICAgICAgaWYgKHdpbmRvdy5mb3JtX3NhdmVkKSB7XG4gICAgICAgIHdpbmRvdy5mb3JtX3NhdmVkID0gZmFsc2U7XG4gICAgICAgICQoJy5mb3JtX3NhdmVfcGFnZScpLnJlbW92ZUNsYXNzKCdoaWRkZW4nKTtcbiAgICAgICAgcmV0dXJuICQoJ2RpdiNmb3JtYWZmaXgnKS5yZW1vdmVDbGFzcygnaGlkZGVuJyk7XG4gICAgICB9XG4gICAgfTtcbiAgICB3aW5kb3cubWFya19zYXZlZCA9IGZ1bmN0aW9uKCkge1xuICAgICAgaWYgKCF3aW5kb3cuZm9ybV9zYXZlZCkge1xuICAgICAgICB3aW5kb3cuZm9ybV9zYXZlZCA9IHRydWU7XG4gICAgICAgICQoJy5mb3JtX3NhdmVfcGFnZScpLmFkZENsYXNzKCdoaWRkZW4nKTtcbiAgICAgICAgcmV0dXJuICQoJ2RpdiNmb3JtYWZmaXgnKS5hZGRDbGFzcygnaGlkZGVuJyk7XG4gICAgICB9XG4gICAgfTtcbiAgICBmb3JtaWQgPSAkKCdpbnB1dFtuYW1lPVwiaWRcIl0nKS52YWwoKTtcbiAgICBpZiAoZm9ybWlkKSB7XG4gICAgICB3aW5kb3cuZm9ybV9zYXZlZCA9IGZhbHNlO1xuICAgICAgbWFya19zYXZlZCgpO1xuICAgIH0gZWxzZSB7XG4gICAgICB3aW5kb3cuZm9ybV9zYXZlZCA9IHRydWU7XG4gICAgICBtYXJrX3Vuc2F2ZWQoKTtcbiAgICB9XG4gICAgJCgnZm9ybSNwYWdlZm9ybScpLm9uKCdjaGFuZ2UnLCAnLmlyc2Zvcm0gaW5wdXQsIC5pcnNmb3JtIHNlbGVjdCwgLmlyc2Zvcm0gdGV4dGFyZWEnLCBmdW5jdGlvbigpIHtcbiAgICAgIHZhciBlbGVtO1xuICAgICAgZWxlbSA9ICQodGhpcyk7XG4gICAgICBtYXJrX3Vuc2F2ZWQoZWxlbSk7XG4gICAgICByZXR1cm4gdHJ1ZTtcbiAgICB9KTtcbiAgICAkKCdmb3JtI3BhZ2Vmb3JtJykub24oJ3N3aXRjaENoYW5nZS5ib290c3RyYXBTd2l0Y2gnLCAnLmlyc2Zvcm0gaW5wdXQudG9nZ2xlLWNoa2JveCcsIGZ1bmN0aW9uKGV2ZW50LCBzdGF0ZSkge1xuICAgICAgdmFyIGVsZW07XG4gICAgICBlbGVtID0gJCh0aGlzKTtcbiAgICAgIG1hcmtfdW5zYXZlZChlbGVtKTtcbiAgICAgIHJldHVybiB0cnVlO1xuICAgIH0pO1xuICAgIHdpbmRvdy5zdWJtaXRfaXJzX2Zvcm0gPSBmdW5jdGlvbihuZXh0X3BhZ2UsIHNhdmUpIHtcbiAgICAgIHZhciBhbGxfaW5wdXRzLCBhbGxfc2VsZWN0cywgYWxsX3RleHRhcmVhcywgZWNvdW50LCBmb3JtX2RhdGEsIGZvcm1fbmFtZSwgZm9ybV9zZWxlY3RvciwgcHJvY2Vzc19lbGVtZW50cywgc3JjX3VybCwgdjtcbiAgICAgIHdpbmRvdy52YWxpZGF0aW5nX2Zvcm0gPSBcIlwiO1xuICAgICAgZm9ybV9zZWxlY3RvciA9IFwiI3BhZ2Vmb3JtXCI7XG4gICAgICBmb3JtX2RhdGEgPSB7fTtcbiAgICAgIGZvcm1fZGF0YVsnZG9fZm9ybV9zYXZlJ10gPSBzYXZlO1xuICAgICAgZm9ybV9uYW1lID0gJ21haW5mb3JtJztcbiAgICAgIGVjb3VudCA9IDA7XG4gICAgICBwcm9jZXNzX2VsZW1lbnRzID0gZnVuY3Rpb24oZWxlbWVudHMpIHtcbiAgICAgICAgcmV0dXJuIGVsZW1lbnRzLmVhY2goZnVuY3Rpb24oKSB7XG4gICAgICAgICAgdmFyIG5hbWUsIHR5cGUsIHZhbHVlO1xuICAgICAgICAgIG5hbWUgPSAkKHRoaXMpLmF0dHIoJ25hbWUnKTtcbiAgICAgICAgICB0eXBlID0gJCh0aGlzKS5hdHRyKCd0eXBlJyk7XG4gICAgICAgICAgdmFsdWUgPSAkKHRoaXMpLnZhbCgpO1xuICAgICAgICAgIGlmICh0eXBlID09PSAnY2hlY2tib3gnKSB7XG4gICAgICAgICAgICB2YWx1ZSA9ICQodGhpcykuZGF0YShcImJvb3RzdHJhcC1zd2l0Y2hcIikuc3RhdGUoKTtcbiAgICAgICAgICB9XG4gICAgICAgICAgZm9ybV9kYXRhW25hbWVdID0gdmFsdWU7XG4gICAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICAgIH0pO1xuICAgICAgfTtcbiAgICAgIGFsbF9pbnB1dHMgPSAkKGZvcm1fc2VsZWN0b3IgKyBcIiBpbnB1dFwiKTtcbiAgICAgIGFsbF9zZWxlY3RzID0gJChmb3JtX3NlbGVjdG9yICsgXCIgc2VsZWN0XCIpO1xuICAgICAgYWxsX3RleHRhcmVhcyA9ICQoZm9ybV9zZWxlY3RvciArIFwiIHRleHRhcmVhXCIpO1xuICAgICAgdiA9IHByb2Nlc3NfZWxlbWVudHMoYWxsX2lucHV0cyk7XG4gICAgICB2ID0gcHJvY2Vzc19lbGVtZW50cyhhbGxfc2VsZWN0cyk7XG4gICAgICB2ID0gcHJvY2Vzc19lbGVtZW50cyhhbGxfdGV4dGFyZWFzKTtcbiAgICAgIGlmICgodHlwZW9mIGZvcm00NDNhX3BhZ2UgIT09IFwidW5kZWZpbmVkXCIgJiYgZm9ybTQ0M2FfcGFnZSAhPT0gbnVsbCkgJiYgZm9ybTQ0M2FfcGFnZSA9PT0gJ2lzX3BhZ2U2X2FjdGl2ZScpIHtcbiAgICAgICAgZm9ybV9kYXRhWyduZXRfYnVzaW5lc3NfaW5jb21lJ10gPSAwO1xuICAgICAgfVxuICAgICAgc3JjX3VybCA9ICQod2luZG93LnZhbGlkYXRpbmdfZm9ybSkuYXR0cignYWN0aW9uJyk7XG4gICAgICAkLmFqYXgoc3JjX3VybCwge1xuICAgICAgICB0eXBlOiAnUE9TVCcsXG4gICAgICAgIGRhdGFUeXBlOiAnaHRtbCcsXG4gICAgICAgIGRhdGE6ICQucGFyYW0oZm9ybV9kYXRhKSxcbiAgICAgICAgc3VjY2VzczogZnVuY3Rpb24oZGF0YSwgdGV4dFN0YXR1cywganFYSFIpIHtcbiAgICAgICAgICB2YXIgZXJyb3JsaXN0LCBlcnJvcnMsIGVycm9ydHh0LCBldHh0LCBmaWVsZG5hbWUsIGksIGosIGpzZGF0YSwgbGVuLCBsZW4xO1xuICAgICAgICAgICQoJ3VsLmVycm9ybGlzdCcpLnJlbW92ZSgpO1xuICAgICAgICAgIGlmIChkYXRhICE9PSAnT0snKSB7XG4gICAgICAgICAgICBqc2RhdGEgPSBKU09OLnBhcnNlKGRhdGEpO1xuICAgICAgICAgICAgZm9yIChpID0gMCwgbGVuID0ganNkYXRhLmxlbmd0aDsgaSA8IGxlbjsgaSsrKSB7XG4gICAgICAgICAgICAgIGVycm9ycyA9IGpzZGF0YVtpXTtcbiAgICAgICAgICAgICAgZmllbGRuYW1lID0gZXJyb3JzWzBdO1xuICAgICAgICAgICAgICBlcnJvcmxpc3QgPSBlcnJvcnNbMV07XG4gICAgICAgICAgICAgIGVycm9ydHh0ID0gJzx1bCBjbGFzcz1cImVycm9ybGlzdFwiPic7XG4gICAgICAgICAgICAgIGZvciAoaiA9IDAsIGxlbjEgPSBlcnJvcmxpc3QubGVuZ3RoOyBqIDwgbGVuMTsgaisrKSB7XG4gICAgICAgICAgICAgICAgZXR4dCA9IGVycm9ybGlzdFtqXTtcbiAgICAgICAgICAgICAgICBlcnJvcnR4dCArPSBcIjxsaT5cIiArIGV0eHQgKyBcIjwvbGk+XCI7XG4gICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgZXJyb3J0eHQgKz0gJzwvdWw+JztcbiAgICAgICAgICAgICAgJChlcnJvcnR4dCkuaW5zZXJ0QWZ0ZXIoJ2xhYmVsW2Zvcio9XCJpZF8nICsgZmllbGRuYW1lICsgJ1wiXScpO1xuICAgICAgICAgICAgfVxuICAgICAgICAgICAgZm9ybV92YWxpZGF0ZWQoZm9ybV9uYW1lLCAyKTtcbiAgICAgICAgICAgIGFsZXJ0KFwiU29tZSBmaWVsZHMgYXJlIGZpbGxlZCBpbmNvcnJlY3RseS5cXG5QbGVhc2UgZml4IGlzc3VlcyBhbmQgc3VibWl0IHRoZSBmb3JtIGFnYWluLlwiKTtcbiAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgZm9ybV92YWxpZGF0ZWQoZm9ybV9uYW1lLCAwKTtcbiAgICAgICAgICAgIGlmIChzYXZlKSB7XG4gICAgICAgICAgICAgIG1hcmtfc2F2ZWQoKTtcbiAgICAgICAgICAgICAgaWYgKCQoJy5mb3JtLWlkW3ZhbHVlPVwiXCJdJykubGVuZ3RoID4gMCAmJiAhbmV4dF9wYWdlKSB7XG4gICAgICAgICAgICAgICAgbmV4dF9wYWdlID0gd2luZG93LmxvY2F0aW9uLmhyZWY7XG4gICAgICAgICAgICAgIH1cbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIGlmIChuZXh0X3BhZ2UpIHtcbiAgICAgICAgICAgICAgd2luZG93LmxvY2F0aW9uLmhyZWYgPSBuZXh0X3BhZ2U7XG4gICAgICAgICAgICAgIHJldHVybiBmYWxzZTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIHJldHVybiB0cnVlO1xuICAgICAgICAgIH1cbiAgICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICAgIH1cbiAgICAgIH0pO1xuICAgICAgcmV0dXJuIGZhbHNlO1xuICAgIH07XG4gICAgJChkb2N1bWVudCkub24oXCJjbGlja1wiLCBcIi5pcnNmb3JtLWZvcm0tc2F2ZVwiLCBmdW5jdGlvbigpIHtcbiAgICAgIHZhciBuZXh0X3BhZ2U7XG4gICAgICBuZXh0X3BhZ2UgPSAkKHRoaXMpLmRhdGEoJ3VybCcpO1xuICAgICAgc3VibWl0X2lyc19mb3JtKG5leHRfcGFnZSwgdHJ1ZSk7XG4gICAgICByZXR1cm4gZmFsc2U7XG4gICAgfSk7XG4gICAgcmV0dXJuIHdpbmRvdy5vbmJlZm9yZXVubG9hZCA9IGZ1bmN0aW9uKCkge1xuICAgICAgaWYgKHdpbmRvdy5mb3JtX3NhdmVkKSB7XG4gICAgICAgIHJldHVybiB2b2lkIDA7XG4gICAgICB9XG4gICAgICBzdWJtaXRfaXJzX2Zvcm0obnVsbCwgZmFsc2UpO1xuICAgICAgcmV0dXJuICcgJztcbiAgICB9O1xuICB9XG59KTtcbiIsIid1c2Ugc3RyaWN0JztcbiQoZnVuY3Rpb24oKSB7fSk7XG4iLCIndXNlIHN0cmljdCc7XG4kKGZ1bmN0aW9uKCkge1xuICB2YXIgbW9udGhOYW1lcztcbiAgbW9udGhOYW1lcyA9IFtcIkphbnVhcnlcIiwgXCJGZWJydWFyeVwiLCBcIk1hcmNoXCIsIFwiQXByaWxcIiwgXCJNYXlcIiwgXCJKdW5lXCIsIFwiSnVseVwiLCBcIkF1Z3VzdFwiLCBcIlNlcHRlbWJlclwiLCBcIk9jdG9iZXJcIiwgXCJOb3ZlbWJlclwiLCBcIkRlY2VtYmVyXCJdO1xuICAkKCcjb2ljX2NhbGNfYnRuJykuY2xpY2soZnVuY3Rpb24oKSB7XG4gICAgdmFyIGNsaWVudF9pZCwgZWxlbWlkLCBtb2RhbGZvcm0sIHVybDtcbiAgICBlbGVtaWQgPSAkKHRoaXMpLmRhdGEoJ2lkJyk7XG4gICAgdXJsID0gJCh0aGlzKS5kYXRhKCdzb3VyY2V1cmwnKTtcbiAgICBpZiAoJCgnI29iamVjdF9kYXRhLmNsaWVudC1pZCcpLmxlbmd0aCA+IDApIHtcbiAgICAgIGNsaWVudF9pZCA9ICQoJyNvYmplY3RfZGF0YS5jbGllbnQtaWQnKS5kYXRhKCdvYmplY3RpZCcpO1xuICAgICAgdXJsID0gXCJcIiArIHVybCArIGNsaWVudF9pZDtcbiAgICB9XG4gICAgbW9kYWxmb3JtID0gJChcIi5tb2RhbC1lbGVtZW50XCIpO1xuICAgICQuYWpheCh1cmwsIHtcbiAgICAgIHR5cGU6ICdHRVQnLFxuICAgICAgZGF0YVR5cGU6ICdodG1sJyxcbiAgICAgIHN1Y2Nlc3M6IGZ1bmN0aW9uKGRhdGEsIHRleHRTdGF0dXMsIGpxWEhSKSB7XG4gICAgICAgICQobW9kYWxmb3JtKS5odG1sKGRhdGEpO1xuICAgICAgICByZWluaXRXaWRnZXRzKCk7XG4gICAgICAgICQoJy5tb2RhbGZvcm0nLCBtb2RhbGZvcm0pLm1vZGFsKHtcbiAgICAgICAgICBzaG93OiB0cnVlXG4gICAgICAgIH0sIHtcbiAgICAgICAgICBrZXlib2FyZDogdHJ1ZVxuICAgICAgICB9KTtcbiAgICAgICAgJCgnLm1vZGFsIC5mb3Jtc2F2ZWJ0bicsIG1vZGFsZm9ybSkuY2xpY2soZnVuY3Rpb24oKSB7XG4gICAgICAgICAgJCgnZm9ybScsIG1vZGFsZm9ybSkuYWpheFN1Ym1pdCgpO1xuICAgICAgICAgIHJldHVybiAkKCcubW9kYWxmb3JtJywgbW9kYWxmb3JtKS5tb2RhbCgnaGlkZScpO1xuICAgICAgICB9KTtcbiAgICAgICAgb2ljX2NhbGN1bGF0b3IoKTtcbiAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgICAgfVxuICAgIH0pO1xuICAgIHJldHVybiBmYWxzZTtcbiAgfSk7XG4gIHdpbmRvdy5vaWNfY2FsY3VsYXRvciA9IGZ1bmN0aW9uKCkge1xuICAgIHZhciBhZGRheSwgYWRtb250aCwgYWR5ZWFyLCBjYW5fcGF5LCBkZWJ0LCBleHBkYXRlLCBpbmNvbWUsIG1vbnRocywgbm93dGltZSwgb2Ftb3VudCwgc3VnZ19hbW91bnQ7XG4gICAgY29uc29sZS5sb2coXCJvaWNfY2FsY3VsYXRvclwiKTtcbiAgICBhZG1vbnRoID0gbXlwYXJzZUludCgkKCcjaWRfcHBfYXNzZXNzZWRfZGF0ZV9tb250aCcpLnZhbCgpKSAtIDE7XG4gICAgYWRkYXkgPSBteXBhcnNlSW50KCQoJyNpZF9wcF9hc3Nlc3NlZF9kYXRlX2RheScpLnZhbCgpKTtcbiAgICBhZHllYXIgPSBteXBhcnNlSW50KCQoJyNpZF9wcF9hc3Nlc3NlZF9kYXRlX3llYXInKS52YWwoKSk7XG4gICAgaWYgKGFkbW9udGggPT09IDAgfHwgYWRkYXkgPT09IDAgfHwgYWR5ZWFyID09PSAwKSB7XG4gICAgICAkKCcucHAtY2FsY3VsYXRpb24nKS5oaWRlKCk7XG4gICAgfSBlbHNlIHtcbiAgICAgIGV4cGRhdGUgPSBuZXcgRGF0ZShhZHllYXIgKyAxMCwgYWRtb250aCwgYWRkYXkpO1xuICAgICAgbm93dGltZSA9IG5ldyBEYXRlKCk7XG4gICAgICBtb250aHMgPSAoKGV4cGRhdGUgLSBub3d0aW1lKSAvICgxMDAwICogNjAgKiA2MCAqIDI0ICogMzAuNDQpKS50b0ZpeGVkKCk7XG4gICAgICAkKCcjcHBfc3RhdHV0ZV9leHBfZGF0ZScpLmh0bWwoKGFkbW9udGggKyAxKSArIFwiLVwiICsgYWRkYXkgKyBcIi1cIiArIChhZHllYXIgKyAxMCkpO1xuICAgICAgJCgnI3BwX3N0YXR1dGVfbW9udGhzX2F2YWlsJykuaHRtbChtb250aHMgKyBcIiBtb250aHNcIik7XG4gICAgICBpbmNvbWUgPSBteXBhcnNlSW50KCQoJyNpZF9wcF9tb250aGx5X2luY29tZScpLnZhbCgpKTtcbiAgICAgIGRlYnQgPSBteXBhcnNlSW50KCQoJyNpZF9wcF9kZWJ0X3RvdGFsJykudmFsKCkpO1xuICAgICAgY2FuX3BheSA9IG1vbnRocyAqIGluY29tZTtcbiAgICAgICQoJyNwcF9jYW5fcGF5JykuaHRtbChcIlwiICsgY2FuX3BheSkua2V5dXAoKTtcbiAgICAgIGlmIChjYW5fcGF5IDwgZGVidCkge1xuICAgICAgICAkKCcjcHBfc3VnZ2VzdGlvbl9xdWFsaWZ5JykuaHRtbCgnTUFZIGJlJyk7XG4gICAgICB9IGVsc2Uge1xuICAgICAgICAkKCcjcHBfc3VnZ2VzdGlvbl9xdWFsaWZ5JykuaHRtbCgnTk9UJyk7XG4gICAgICB9XG4gICAgICBzdWdnX2Ftb3VudCA9IGluY29tZSAqIDEyO1xuICAgICAgJCgnI3BwX3N1Z2dlc3RlZF9hbW91bnQnKS5odG1sKFwiXCIgKyBzdWdnX2Ftb3VudCkua2V5dXAoKTtcbiAgICAgIG9hbW91bnQgPSBteXBhcnNlSW50KCQoJyNpZF9wcF9vZmZlcl9hbW91bnQnKS52YWwoKSk7XG4gICAgICAkKCcjaWRfcHBfb2ZmZXJfYW1vdW50JykudmFsKHN1Z2dfYW1vdW50KS5rZXl1cCgpO1xuICAgICAgJCgnLnBwLWNhbGN1bGF0aW9uJykuc2hvdygpO1xuICAgIH1cbiAgICBvaWNfY2FsY3VsYXRvcjIoKTtcbiAgICByZXR1cm4gdHJ1ZTtcbiAgfTtcbiAgd2luZG93Lm9pY19jYWxjdWxhdG9yMiA9IGZ1bmN0aW9uKCkge1xuICAgIHZhciBjbnQsIGksIGluaXRpYWxfcGF5bWVudCwgaiwgb2Ftb3VudCwgcmVtYWluaW5nX2JhbGFuY2UsIHZhbHVlO1xuICAgIG9hbW91bnQgPSBteXBhcnNlSW50KCQoJyNpZF9wcF9vZmZlcl9hbW91bnQnKS52YWwoKSk7XG4gICAgY29uc29sZS5sb2coXCJvaWNfY2FsY3VsYXRvcjIsIG9hbW91bnQ6IFwiICsgb2Ftb3VudCk7XG4gICAgaWYgKCFvYW1vdW50IHx8IG9hbW91bnQgPT09IDApIHtcbiAgICAgICQoJy5wcC1jYWxjdWxhdGlvbjInKS5oaWRlKCk7XG4gICAgfSBlbHNlIHtcbiAgICAgIGluaXRpYWxfcGF5bWVudCA9IChvYW1vdW50IC8gNSkudG9GaXhlZCgpO1xuICAgICAgJCgnI3BwX2luaXRpYWxfcGF5bWVudCcpLmh0bWwoaW5pdGlhbF9wYXltZW50KS5rZXl1cCgpO1xuICAgICAgcmVtYWluaW5nX2JhbGFuY2UgPSBvYW1vdW50IC0gaW5pdGlhbF9wYXltZW50O1xuICAgICAgY250ID0gNjtcbiAgICAgIGZvciAoaSA9IGogPSAxOyBqIDw9IDU7IGkgPSArK2opIHtcbiAgICAgICAgdmFsdWUgPSAocmVtYWluaW5nX2JhbGFuY2UgLyAoY250IC0gaSkpLnRvRml4ZWQoKTtcbiAgICAgICAgcmVtYWluaW5nX2JhbGFuY2UgPSByZW1haW5pbmdfYmFsYW5jZSAtIHZhbHVlO1xuICAgICAgICAkKFwiI3BwX3BheW1lbnRfXCIgKyBpKS5odG1sKHZhbHVlKS5rZXl1cCgpO1xuICAgICAgfVxuICAgICAgJCgnLnBwLWNhbGN1bGF0aW9uMicpLnNob3coKTtcbiAgICB9XG4gICAgcmV0dXJuIHRydWU7XG4gIH07XG4gICQoZG9jdW1lbnQpLm9uKCdrZXl1cCcsICcub2ljLWNhbGN1bGF0b3IgaW5wdXQnLCBmdW5jdGlvbigpIHtcbiAgICByZXR1cm4gb2ljX2NhbGN1bGF0b3IoKTtcbiAgfSk7XG4gICQoZG9jdW1lbnQpLm9uKCdjaGFuZ2UnLCAnLm9pYy1jYWxjdWxhdG9yIGlucHV0JywgZnVuY3Rpb24oKSB7XG4gICAgcmV0dXJuIG9pY19jYWxjdWxhdG9yKCk7XG4gIH0pO1xuICAkKGRvY3VtZW50KS5vbignY2hhbmdlJywgJy5vaWMtY2FsY3VsYXRvciBzZWxlY3QnLCBmdW5jdGlvbigpIHtcbiAgICByZXR1cm4gb2ljX2NhbGN1bGF0b3IoKTtcbiAgfSk7XG4gICQoZG9jdW1lbnQpLm9uKCdrZXl1cCcsICcjaWRfcHBfb2ZmZXJfYW1vdW50JywgZnVuY3Rpb24oKSB7XG4gICAgcmV0dXJuIG9pY19jYWxjdWxhdG9yMigpO1xuICB9KTtcbiAgcmV0dXJuICQoZG9jdW1lbnQpLm9uKCdjaGFuZ2UnLCAnI2lkX3BwX29mZmVyX2Ftb3VudCcsIGZ1bmN0aW9uKCkge1xuICAgIHJldHVybiBvaWNfY2FsY3VsYXRvcjIoKTtcbiAgfSk7XG59KTtcbiIsIid1c2Ugc3RyaWN0JztcbiQoZnVuY3Rpb24oKSB7XG4gIHZhciBhc2Nzb3J0LCBjdXJwYWdlLCBkaXNhYmxlRXZlbnRzLCBuYXZpZ2F0ZSwgcmVmLCBzb3J0ZmllbGQ7XG4gIGN1cnBhZ2UgPSAxO1xuICBzb3J0ZmllbGQgPSAkKCcucGFnaW5hdGlvbi1zb3J0ZmllbGQnKS5kYXRhKCdmaWVsZCcpO1xuICBhc2Nzb3J0ID0gJCgnLnBhZ2luYXRpb24tc29ydGZpZWxkJykuZGF0YSgnYXNjJyk7XG4gIGlmICgocmVmID0gXCJcIiArIGFzY3NvcnQpICE9PSAnMCcgJiYgcmVmICE9PSAnMScpIHtcbiAgICBhc2Nzb3J0ID0gXCIxXCI7XG4gIH1cbiAgZGlzYWJsZUV2ZW50cyA9IGZhbHNlO1xuICBuYXZpZ2F0ZSA9IGZ1bmN0aW9uKHBhZ2UpIHtcbiAgICB2YXIgZXh0cmF2YXJzLCBmbmFtZSwgZnZhbHVlLCBpLCBqLCBrLCBsLCBsZW4sIGxlbjEsIGxlbjIsIGxlbjMsIGxmaWx0ZXJzLCBsZm8sIHJlZjEsIHJlZjIsIHJlZjMsIHJlZjQ7XG4gICAgaWYgKHBhZ2UgPT0gbnVsbCkge1xuICAgICAgcGFnZSA9IG51bGw7XG4gICAgfVxuICAgIHBhZ2UgPSBwYWdlIHx8IGN1cnBhZ2U7XG4gICAgbGZpbHRlcnMgPSBcIlwiO1xuICAgIHJlZjEgPSAkKCcuaW5wdXQtZmlsdGVyJyk7XG4gICAgZm9yIChpID0gMCwgbGVuID0gcmVmMS5sZW5ndGg7IGkgPCBsZW47IGkrKykge1xuICAgICAgbGZvID0gcmVmMVtpXTtcbiAgICAgIGZuYW1lID0gJChsZm8pLmF0dHIoJ25hbWUnKTtcbiAgICAgIGZ2YWx1ZSA9ICQobGZvKS52YWwoKTtcbiAgICAgIGlmIChmdmFsdWUgIT09ICctJykge1xuICAgICAgICBsZmlsdGVycyArPSBcIiZmaWx0ZXJzW109XCIgKyBmbmFtZSArIFwiKlwiICsgZnZhbHVlO1xuICAgICAgfVxuICAgIH1cbiAgICByZWYyID0gJCgnLmNoay1maWx0ZXInKTtcbiAgICBmb3IgKGogPSAwLCBsZW4xID0gcmVmMi5sZW5ndGg7IGogPCBsZW4xOyBqKyspIHtcbiAgICAgIGxmbyA9IHJlZjJbal07XG4gICAgICBpZiAoJChsZm8pLmlzKFwiOmNoZWNrZWRcIikpIHtcbiAgICAgICAgZm5hbWUgPSAkKGxmbykuYXR0cignbmFtZScpO1xuICAgICAgICBmdmFsdWUgPSAkKGxmbykudmFsKCk7XG4gICAgICAgIGlmIChmdmFsdWUgIT09ICctJykge1xuICAgICAgICAgIGxmaWx0ZXJzICs9IFwiJmZpbHRlcnNbXT1cIiArIGZuYW1lICsgXCIqXCIgKyBmdmFsdWU7XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICB9XG4gICAgcmVmMyA9ICQoJy5saXN0LWZpbHRlcicpO1xuICAgIGZvciAoayA9IDAsIGxlbjIgPSByZWYzLmxlbmd0aDsgayA8IGxlbjI7IGsrKykge1xuICAgICAgbGZvID0gcmVmM1trXTtcbiAgICAgIGZuYW1lID0gJChsZm8pLmF0dHIoJ25hbWUnKTtcbiAgICAgIGZ2YWx1ZSA9ICQobGZvKS52YWwoKTtcbiAgICAgIGlmIChmdmFsdWUgIT09ICctJykge1xuICAgICAgICBsZmlsdGVycyArPSBcIiZmaWx0ZXJzW109XCIgKyBmbmFtZSArIFwiKlwiICsgZnZhbHVlO1xuICAgICAgfVxuICAgIH1cbiAgICBleHRyYXZhcnMgPSBcIlwiO1xuICAgIHJlZjQgPSAkKCcucGFnaW5hdGlvbi1wYXJhbWV0ZXInKTtcbiAgICBmb3IgKGwgPSAwLCBsZW4zID0gcmVmNC5sZW5ndGg7IGwgPCBsZW4zOyBsKyspIHtcbiAgICAgIGxmbyA9IHJlZjRbbF07XG4gICAgICBmbmFtZSA9ICQobGZvKS5kYXRhKCduYW1lJyk7XG4gICAgICBmdmFsdWUgPSAkKGxmbykuZGF0YSgndmFsdWUnKTtcbiAgICAgIGlmIChmdmFsdWUgIT09ICctJykge1xuICAgICAgICBleHRyYXZhcnMgKz0gXCImXCIgKyBmbmFtZSArIFwiPVwiICsgZnZhbHVlO1xuICAgICAgfVxuICAgIH1cbiAgICAkLmFqYXgod2luZG93LmxvY2F0aW9uLnBhdGhuYW1lICsgXCI/JnBhZ2U9XCIgKyBwYWdlICsgbGZpbHRlcnMgKyAoXCImc29ydD1cIiArIHNvcnRmaWVsZCArIFwiJmFzYz1cIiArIGFzY3NvcnQpICsgZXh0cmF2YXJzLCB7XG4gICAgICB0eXBlOiAnR0VUJyxcbiAgICAgIGRhdGFUeXBlOiAnaHRtbCcsXG4gICAgICBzdWNjZXNzOiBmdW5jdGlvbihkYXRhLCB0ZXh0U3RhdHVzLCBqcVhIUikge1xuICAgICAgICB2YXIgaGhoO1xuICAgICAgICBjdXJwYWdlID0gcGFnZTtcbiAgICAgICAgJCgnLnBhZ2luYXRlZF9jb250ZW50JykuaHRtbChkYXRhKTtcbiAgICAgICAgcmVpbml0V2lkZ2V0cygpO1xuICAgICAgICBoaGggPSAkKFwiW2RhdGEtc29ydD0nXCIgKyBzb3J0ZmllbGQgKyBcIiddXCIpLmFkZENsYXNzKCdzb3J0ZmllbGQnKS5odG1sKCk7XG4gICAgICAgIGlmICgoXCJcIiArIGFzY3NvcnQpID09PSAnMScpIHtcbiAgICAgICAgICBoaGggPSBoaGgucmVwbGFjZSgnPC9zcGFuPjwvZGl2PicsICcgPGkgY2xhc3M9XCIgZmEgZmEtc29ydC1hbHBoYS1hc2NcIj48L2k+PC9zcGFuPjwvZGl2PicpO1xuICAgICAgICAgIHJldHVybiAkKFwiW2RhdGEtc29ydD0nXCIgKyBzb3J0ZmllbGQgKyBcIiddXCIpLmFkZENsYXNzKCdzb3J0YXNjJykuaHRtbChoaGgpO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgIGhoaCA9IGhoaC5yZXBsYWNlKCc8L3NwYW4+PC9kaXY+JywgJyA8aSBjbGFzcz1cIiBmYSBmYS1zb3J0LWFscGhhLWRlc2NcIj48L2k+PC9zcGFuPjwvZGl2PicpO1xuICAgICAgICAgIHJldHVybiAkKFwiW2RhdGEtc29ydD0nXCIgKyBzb3J0ZmllbGQgKyBcIiddXCIpLmFkZENsYXNzKCdzb3J0ZGVzYycpLmh0bWwoaGhoKTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH0pO1xuICAgIHJldHVybiBmYWxzZTtcbiAgfTtcbiAgd2luZG93Lm5hdmlnYXRlID0gbmF2aWdhdGU7XG4gICQoZG9jdW1lbnQpLm9uKCdjbGljaycsICcubGlzdG5hdicsIGZ1bmN0aW9uKCkge1xuICAgIHZhciBuZXh0cGFnZTtcbiAgICBuZXh0cGFnZSA9ICQodGhpcykuZGF0YSgncGFnZScpO1xuICAgIGlmICghbmV4dHBhZ2UpIHtcbiAgICAgIHJldHVybiBmYWxzZTtcbiAgICB9XG4gICAgcmV0dXJuIG5hdmlnYXRlKG5leHRwYWdlKTtcbiAgfSk7XG4gICQoZG9jdW1lbnQpLm9uKCdjaGFuZ2UnLCAnLmxpc3QtZmlsdGVyJywgZnVuY3Rpb24oKSB7XG4gICAgaWYgKCFkaXNhYmxlRXZlbnRzKSB7XG4gICAgICByZXR1cm4gbmF2aWdhdGUoMSk7XG4gICAgfVxuICB9KTtcbiAgJChkb2N1bWVudCkub24oJ2NsaWNrJywgJy5jaGstZmlsdGVyJywgZnVuY3Rpb24oKSB7XG4gICAgaWYgKCFkaXNhYmxlRXZlbnRzKSB7XG4gICAgICBuYXZpZ2F0ZSgxKTtcbiAgICB9XG4gICAgcmV0dXJuIHRydWU7XG4gIH0pO1xuICAkKGRvY3VtZW50KS5vbigna2V5dXAnLCAnLmlucHV0LWZpbHRlcicsIGZ1bmN0aW9uKCkge1xuICAgIGlmICghZGlzYWJsZUV2ZW50cykge1xuICAgICAgcmV0dXJuIG5hdmlnYXRlKDEpO1xuICAgIH1cbiAgfSk7XG4gICQoZG9jdW1lbnQpLm9uKCdjbGljaycsICcuZmlsdGVyLXJlc2V0JywgZnVuY3Rpb24oKSB7XG4gICAgdmFyIGksIGosIGxlbiwgbGVuMSwgcmVmMSwgcmVmMiwgc2Vsb2JqO1xuICAgIGRpc2FibGVFdmVudHMgPSB0cnVlO1xuICAgIHJlZjEgPSAkKFwiLmlucHV0LWZpbHRlclwiKTtcbiAgICBmb3IgKGkgPSAwLCBsZW4gPSByZWYxLmxlbmd0aDsgaSA8IGxlbjsgaSsrKSB7XG4gICAgICBzZWxvYmogPSByZWYxW2ldO1xuICAgICAgJChzZWxvYmopLnZhbCgnJyk7XG4gICAgfVxuICAgIHJlZjIgPSAkKFwiLmxpc3QtZmlsdGVyXCIpO1xuICAgIGZvciAoaiA9IDAsIGxlbjEgPSByZWYyLmxlbmd0aDsgaiA8IGxlbjE7IGorKykge1xuICAgICAgc2Vsb2JqID0gcmVmMltqXTtcbiAgICAgICQoc2Vsb2JqKS5zZWxlY3QyKCd2YWwnLCAnLScpO1xuICAgIH1cbiAgICBkaXNhYmxlRXZlbnRzID0gZmFsc2U7XG4gICAgcmV0dXJuIG5hdmlnYXRlKDEpO1xuICB9KTtcbiAgJChkb2N1bWVudCkub24oJ2NsaWNrJywgJ1tkYXRhLXNvcnRdJywgZnVuY3Rpb24oKSB7XG4gICAgdmFyIG15c29ydGZpZWxkO1xuICAgIG15c29ydGZpZWxkID0gJCh0aGlzKS5kYXRhKCdzb3J0Jyk7XG4gICAgaWYgKHNvcnRmaWVsZCA9PT0gbXlzb3J0ZmllbGQpIHtcbiAgICAgIGFzY3NvcnQgPSBhc2Nzb3J0IF4gMTtcbiAgICB9IGVsc2Uge1xuICAgICAgYXNjc29ydCA9IDE7XG4gICAgICBzb3J0ZmllbGQgPSBteXNvcnRmaWVsZDtcbiAgICB9XG4gICAgcmV0dXJuIG5hdmlnYXRlKCk7XG4gIH0pO1xuICBpZiAoJCgnLnBhZ2luYXRlZF9jb250ZW50JykubGVuZ3RoID4gMCkge1xuICAgIHJldHVybiBuYXZpZ2F0ZSgxKTtcbiAgfVxufSk7XG4iXX0=

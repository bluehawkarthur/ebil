$.ajax({
      url: '/configfactura/',
      dataType: 'json',
      type: 'GET',
      success: function(datos) {


      if (datos[0].fields.descuento_usar == false) {
        // $( "#id_codigo_fabrica" ).prop( "disabled", true );
        $( ".input-descuento" ).css( "display", 'none' );
        $("#help_cod .help-block").prop("hidden", true);
        $( "#add_descuentoc" ).removeClass( "invalid" )

      }

      if (datos[0].fields.descuento_requerido == false) {
        // $("#add_descuentoc").val("");
        $("#help_cod .help-block").prop("hidden", true);
        $( "#add_descuentoc" ).removeClass( "invalid" )
      }else{
        $("#add_descuentoc").prop("required", true);
      }

      if (datos[0].fields.recargo_usar == false) {
        // $( "#id_codigo_fabrica" ).prop( "disabled", true );
        $( ".input-recargo" ).css( "display", 'none' );
        $("#help_cod .help-block").prop("hidden", true);
        $( "#add_recargoc" ).removeClass( "invalid" )

      }

      if (datos[0].fields.recargo_requerido == false) {
        // $("#add_recargoc").val("");
        $("#help_cod .help-block").prop("hidden", true);
        $( "#add_recargoc" ).removeClass( "invalid" )
      }else{
        $("#add_recargoc").prop("required", true);
      }

      if (datos[0].fields.ice_usar == false) {
        // $( "#id_codigo_fabrica" ).prop( "disabled", true );
        $( ".input-ice" ).css( "display", 'none' );
        $("#help_cod .help-block").prop("hidden", true);
        $( "#add_icec" ).removeClass( "invalid" )

      }

      if (datos[0].fields.ice_requerido == false) {
        // $("#add_icec").val("");
        $("#help_cod .help-block").prop("hidden", true);
        $( "#add_icec" ).removeClass( "invalid" )
      }else{
        $("#add_icec").prop("required", true);
      }

     if (datos[0].fields.exentos_usar == false) {
      // $( "#id_codigo_fabrica" ).prop( "disabled", true );
      $( ".input-excento" ).css( "display", 'none' );
      $("#help_cod .help-block").prop("hidden", true);
      $( "#add_exentosc" ).removeClass( "invalid" )

      }

      if (datos[0].fields.exentos_requerido == false) {
        // $("#add_exentosc").val("");
        $("#help_cod .help-block").prop("hidden", true);
        $( "#add_exentosc" ).removeClass( "invalid" )
      }else{
        $("#add_exentosc").prop("required", true);
      }

      if (datos[0].fields.tipos_venta_usar == false) {
      // $( "#id_codigo_fabrica" ).prop( "disabled", true );
      $( ".input-tipo" ).css( "display", 'none' );
      $("#help_cod .help-block").prop("hidden", true);
      $( "#add_exentosc" ).removeClass( "invalid" )

      }

      } //success
});

var fullDate = new Date();
var twoDigitMonth = ((fullDate.getMonth().length+1) === 1)? (fullDate.getMonth()+1) : (fullDate.getMonth()+1);

var currentDate =  fullDate.getFullYear()+ "-" + twoDigitMonth + "-" + fullDate.getDate();

console.log(currentDate);
$("#add_fecha").val(currentDate);

// para recorrer inputs presionando enter ===========
$(document).ready(function () {
    $(".EntTab").bind("keypress", function(e) {

        if (e.keyCode == 13) {
            var inps = $("input, select"); //add select too
            for (var x = 0; x < inps.length; x++) {
                if (inps[x] == this) {
                    while ((inps[x]).name == (inps[x + 1]).name) {
                    x++;
                    }
                    if ((x + 1) < inps.length) $(inps[x + 1]).focus();
                }
            }   e.preventDefault();
        }
    });
});


//============= corregir sta con errores de cantidad ==========================
//=============================================================================
$("#add_cantidad").keyup(function(){
      if ( $( "#add_cantidad" ).val()<= parseInt($( "#stock_add").val()) && $( "#add_cantidad" ).val() > 0){

      }else{
        if ($( "#add_cantidad" ).val() == '') {

        }else{
          $( "#add_cantidad" ).val('');
          $.bootstrapGrowl("No existe la cantidad de items disponibles que coloco", {
              type: 'danger',
              offset: {from: 'top', amount: 150},
              align: 'center',
              width: 350,
              allow_dismiss: false
          });
        }
        
      };
}); 
// ==================== hasta aqui =========================================

//====== codigo para desabilitar inputs de almacen =========
// code for disable input is codigo item)===========
function disable() {
  $(".add_disable").attr('disabled', 'disabled');
  $(".add_total").attr('disabled', 'disabled');
  $(".add_scf").attr('disabled', 'disabled');
}

disable();

// ===== codigo para tipo de compra credito ================

$("#input-credito").hide();

$("#add_tipo").change(function(){
  var dato = $(this).val();
  console.log(dato);
  if ($(this).is(':checked')){
     // validador
    $('#save').prop('disabled', 'disabled');
         
    $("#input-credito").show();
  }else{
    
    
    $("#input-credito").hide();
    $("#dias").val('');
    // validador
    if ($("#encabezado").valid() && proceso.producto.length > 0) {
        $('#save').prop('disabled', false);  
    } 
  }
}); 

// ======== validadorrrrrr =====================================0
$('#save').prop('disabled', true); 
$('input').on('blur keyup', function() {
    if ($("#encabezado").valid() && proceso.producto.length > 0) {
        $('#save').prop('disabled', false);  
    } else {
        $('#save').prop('disabled', 'disabled');
    }
});

$("#encabezado").validate({
    rules: {
        
        add_razon: {
            required: true,
           
        },
        add_fecha: {
            required: true,
         
        },
        dias: {
            required: true,
         
        }
    }
});

$("#movimiento").change(function(){
      var dato = $(this).val();
      
      if (dato == 'baja'){
        $("#add_nit").attr('disabled', 'disabled');
        $("#add_razon").attr('disabled', 'disabled');
        $("#add_nit").prop('required', false);
        $("#add_nit").removeClass('invalid');
        if ($("#encabezado").valid() && proceso.producto.length > 0) {
            $('#save').prop('disabled', false);  
        } else {
            $('#save').prop('disabled', 'disabled');
        }

      }else if (dato == 'proforma'){
        // validar el nittttttt
        $("#add_nit").prop('required', false);
        $('#add_nit').prop('disabled', false); 
        $('#add_razon').prop('disabled', false);
        if ($("#encabezado").valid() && proceso.producto.length > 0) {
            $('#save').prop('disabled', false);  
        } else {
            $('#save').prop('disabled', 'disabled');
        }
      }else if (dato == 'facturar'){
        // validar el nittttttt
        $("#add_nit").attr('required', 'required');
        $('#add_nit').prop('disabled', false); 
        $('#add_razon').prop('disabled', false);
        if ($("#encabezado").valid() && proceso.producto.length > 0) {
            $('#save').prop('disabled', false);  
        } else {
            $('#save').prop('disabled', 'disabled');
        }

      }else{
        $('#add_nit').prop('disabled', false); 
        $('#add_razon').prop('disabled', false);
      }
}); 



// objeto para guardar productos y factura de la compra
var proceso = new Object();
proceso.producto = new Array();
console.log('el rpdoctooooooooooooo')
console.log();
var table = new Array();
function agregarDetalle(){
  console.log('----datosss array ------------');
    if ($( "#stock_add" ).val() > 0){
      // para abrir en una nueva ventana 
      // $("#post_form").prop("target", '_blank');

      console.log($( "#stock_add" ).val());
      // var cant = $( "#add_cantidad" ).val();
      // table.push({'cantidad':cant});
      // console.log(table);
      var d = table;
      //para limpiar progreso d circulo
      $('#circle').circleProgress({
                value: 0,
                size: 0,        
      });
      //limpiar texto d stock
      $('#stock').html('');

      var item =  $( "#add_codigo_item" ).val();
      var centroC =  $( "#add_costos" ).val();
      console.log('costosssssssss');
      console.log(centroC);
      var cantidad =  $( "#add_cantidad" ).val();

       // condicon de typo descuento 
      var typo_descuento= $("#add_fk_id_formato_dato_descuento").val();
      if (typo_descuento==475){
        typo_descuento = '%'; 
      }else{
        typo_descuento = 'Bs'; 
      }

      var typo_recargo= $("#add_fk_id_formato_dato_recargo").val();
      if (typo_recargo==475){
        typo_recargo = '%'; 
      }else{
        typo_recargo = 'Bs'; 
      }


    

      proceso.producto.push({
        'codigo_item': item,
        'pk': $('#pk').val(),
        'cantidad': cantidad,
        'unidad': $('#add_unidad').val(),
        'detalle': $('#add_detalle').val(),
        'precio_unitario': $('#add_precio_unitario').val(),
        'subtotal': $('#add_total').val(),
        'descuentos': $('#add_descuento').val(),
        'recargos': $('#add_recargo').val(),
        'ice': $('#add_ice').val(),
        'excentos': $('#add_exentos').val(),
        'sdf': $('#add_sujeto_credito_fiscal').val(),
        'centro_costos': $('#add_costos').val(),
        'tipo_descuento': typo_descuento,
        'tipo_recargo' : typo_recargo,
       
      });

      console.log(proceso);

      // obteniendo la tabla para insertar los campos
      var t = document.getElementById('tb-detalle').getElementsByTagName('tbody')[0];
      // obteniendo el tr de la tabla
      var rowCount = t.rows.length-1;
          // insertando los  td
          var row = t.insertRow(rowCount);
          // insertando ids a los tr de la tabla
          row.id='tr_'+rowCount;
          //agregando celdas
          var cell1 = row.insertCell(0);
          var cell2 = row.insertCell(1);
          var cell3 = row.insertCell(2);
          var cell4 = row.insertCell(3);
          var cell5 = row.insertCell(4);
          var cell6 = row.insertCell(5);
          var cell7 = row.insertCell(6);
          var cell8 = row.insertCell(7);
          var cell9 = row.insertCell(8);
          var cell10 = row.insertCell(9);
          var cell11 = row.insertCell(10);
          var cell12 = row.insertCell(11);
          var cell13 = row.insertCell(12);

          // insertando los datos en los td
          cell1.innerHTML = rowCount+1;
          cell2.innerHTML = $( "#add_codigo_item" ).val();
          cell3.innerHTML = $( "#add_cantidad" ).val();

          cell4.innerHTML = $( "#add_unidad" ).val();
     
          cell5.innerHTML =  $('#add_detalle').val();
       
          cell6.innerHTML = $('#add_precio_unitario').val();

          cell7.innerHTML = ($('#add_precio_unitario').val())*cantidad;

          var descuento = 0;
          if($('#add_descuento').val()!=''){
              descuento = $('#add_descuento').val();
          }
          cell8.innerHTML = descuento;

          var recargo = 0;
          if($('#add_recargo').val()!=''){
              recargo = $('#add_recargo').val();
          }
          cell9.innerHTML = recargo;

          cell10.innerHTML = $( "#add_ice" ).val();
          cell11.innerHTML = $( "#add_exentos" ).val();


          cell12.innerHTML = $( "#add_sujeto_credito_fiscal" ).val();

          var ct= rowCount+1;
         
          cell13.innerHTML ="<a class='btn-floating waves-effect waves-light red' id='eliminar-"+ct+"'><i class='mdi-action-delete'></i></a>";

          $('#eliminar-'+ct).click(function (){
            console.log('deleteeeeeeeeeeeeeeee');
            row.remove();
            calTotal();
            proceso.producto.splice(ct-1,1);
            console.log(proceso.producto);
          });
          console.log(row);
          calTotal();
          $('#add_detalle').val('');
          $( "#add_codigo_item" ).val('');
          $( "#add_unidad" ).val('');
          $('#add_precio_unitario').val('');
          $( "#add_cantidad" ).val('');
          $('#add_total').val('');
          $('#add_sujeto_credito_fiscal').val('');
          $('#add_buscar_item').val('');
          $('#add_descuento').val(0);
          $('#add_recargo').val(0);

         //======= para validar ==========
         
          
              if ($("#encabezado").valid() && proceso.producto.length > 0) {
                  $('#save').prop('disabled', false);  
              } else {
                  $('#save').prop('disabled', 'disabled');
              }
          
          
          

          }else{
           
            $.bootstrapGrowl("No existe items desponibles", {
                type: 'danger',
                offset: {from: 'top', amount: 150},
                align: 'center',
                width: 350,
                allow_dismiss: false
            });
          }

        }

        var total = 0;
        function calTotal(){
            var total=0;
            var t=0;
            $('#tb-detalle tbody tr').each(function () {
                total = total*1 + $(this).find("td").eq(11).html()*1;  
                
                if (!isNaN(total)) {
                  t = t*1 + $(this).find("td").eq(11).html()*1; 
                  
                };
            });

            console.log(t);
            $('#sum-subtotal').text(t.toFixed(2));
            $('#sum-tax').text(t.toFixed(2));

            $('#sum-total').text(total.toFixed(2));


        }


        function onEnviar(){

            proceso.nit = $('#add_nit').val();
            proceso.razon = $('#add_razon').val();
            proceso.fecha = $('#add_fecha').val();
            proceso.descuento = $('#add_descuentoc').val();
            proceso.recargo = $('#add_recargoc').val();
            proceso.ice = $('#add_icec').val();
            proceso.excentos = $('#add_exentosc').val();


            proceso.tipo_descuento = $('input[name="tipo_descuentoc"]:checked').val();
            proceso.tipo_recargo = $('input[name="tipo_recargoc"]:checked').val();
            proceso.movimiento  = $('#movimiento').val();
            proceso.sucursal = $('#add_sucursal').val();
            proceso.actividad = $('#add_actividad').val();


            var tipo_c= 'contado';
            var dias= 0;
            if ($('#add_tipo').is(':checked')){
              tipo_c = 'credito';
              dias= $('#dias').val();
            }

            proceso.tipo_compra = tipo_c;

            proceso.dias = dias;

            console.log(JSON.stringify(proceso));
           document.getElementById("proceso").value=JSON.stringify(proceso);
        
           // $('#tb-detalle tbody tr').remove();
           var t = document.getElementById('tb-detalle').getElementsByTagName('tbody')[0];
            
            //funcion para eliminar tr por el id 
           function  deleteRow(id) {
              document.getElementById('tb-detalle').getElementsByTagName('tbody')[0].removeChild(
              document.getElementById(id)
              );
           }

          
          // for para contar los tr y eliminarlos
          for (i = 0; i < t.rows.length; i++) {
            console.log(t.rows[i]);
            
            deleteRow('tr_'+i);
            
          }
          // vaciar texto del subtotal de la tabla
          $('#sum-subtotal').text('');

          
          delete proceso['nit'];
          delete proceso['razon'];
          delete proceso['fecha'];
          delete proceso['tipo_compra'];
          delete proceso['dias'];
          delete proceso['descuento'];
          delete proceso['recargo'];
          delete proceso['ice'];
          delete proceso['excentos'];
          delete proceso['tipo_descuento'];
          delete proceso['tipo_recargo'];

          $('#add_nit').val('');
          $('#add_razon').val('');
          // $('#add_fecha').val('');
          $('#dias').val('');
          $('#add_descuentoc').val(0);
          $('#add_recargoc').val(0);
          $('#add_icec').val(0);
          $('#add_exentosc').val(0);
          $("#test1").prop('checked', true);
          $("#teste1").prop('checked', true);
          
          $('#add_tipo').prop('checked', false);
          $("#input-credito").hide();
          proceso.producto = new Array();

             
          $('#save').prop('disabled', true); 

           console.log(proceso);
        }

        
        $(function() {


          $(".add_calculo_totales").change(function(){
            add_calculo_totales();
          }); 

          $(".add_calculo_totales_down").keyup(function(){
            add_calculo_totales();
          }); 

          function add_calculo_totales(){
           var sujetoADF = 0;
           var total = 0 +$("#add_cantidad").val()*$("#add_precio_unitario").val();
           console.log("descuento ------------------");
           console.log($( "#add_fk_id_formato_dato_descuento" ).val());

           sujetoADF= ($( "#add_fk_id_formato_dato_descuento" ).val()==475)?(Number(total)- Number(total*Number($("#add_descuento").val())/100)):(Number(total)- Number($("#add_descuento").val()));

           sujetoADF= ($( "#add_fk_id_formato_dato_recargo" ).val()==475)?(Number(sujetoADF)+ Number(total*$("#add_recargo").val()/100)):(Number(sujetoADF)+ Number($("#add_recargo").val()));

           sujetoADF= Number(sujetoADF)- Number($("#add_ice").val());
           sujetoADF= Number(sujetoADF)- Number($("#add_exentos").val());
           
           // sujetoADF= ($( "#add_fk_id_formato_dato_ice" ).val()==475)?(Number(sujetoADF)- Number(total*$("#add_ice").val()/100)):(Number(sujetoADF)- Number($("#add_ice").val()));
           // sujetoADF= ($( "#add_fk_id_formato_dato_excentos" ).val()==475)?(Number(sujetoADF)- Number(total*$("#add_excentos").val()/100)):(Number(sujetoADF)- Number($("#add_excentos").val()));


           $("#add_total").val(total);
           $("#add_sujeto_credito_fiscal").val(sujetoADF);
          }

         $( "#add_buscar_item" ).autocomplete({

          source: function( request, response ) {
            console.log(request);
            $.ajax({
              url: "/buscar_item2/",
              dataType: "json",
              data: {'id':request.term, 'sucur': 'lleguueeeeeeee'},
              success: function( data ) {
               console.log(data);
               response($.map(data, function (pn) {
                console.log('estoo es stockkkkkkkkkk')
                console.log(pn);
                console.log('uuuuuuuuuuuuuuuuuuuuu')
                return {
                  pk: pn.pk,
                  codigo_item: pn.fields.codigo_item,
                  stock: pn.fields.cantidad,
                  saldo_min: pn.fields.saldo_min,
                  unidad_medida: pn.fields.unidad_medida,
                  descripcion: pn.fields.descripcion,
                  costo_unitario: pn.costo_unitario,
                  precio_unitario: pn.fields.precio_unitario,
                  label: pn.fields.codigo_item+"-"+pn.fields.descripcion
                };
              }));

             }
           });
          }, 
          minLength: 1,       
          select: function( event, ui ) {
            var fila = new Object();
            $(this).val("");
            fila.pk = ui.item.pk_id_item;
            fila.codigo_item = ui.item.codigo_item;
            fila.precio = ui.item.precio_unitario;
            fila.descripcion= ui.item.descripcion;
            fila.cantidad = 1;

            console.log('taaaaaablaaaaaaaaaaaaaaaaaaa');
            table.push(fila);
            console.log(table);
            console.log('taaaaaablaaaaaaaaaaaaaaaaaaa');
            console.log('primaryyyyyyy');
            console.log(ui.item.pk);

            $( "#add_item_detail" ).val( ui.item.label );
            $( "#add_codigo_item" ).val( ui.item.codigo_item );
             $( "#pk" ).val( ui.item.pk );
            $( "#add_detalle" ).val( ui.item.descripcion );

            $( "#add_unidad" ).val( ui.item.unidad_medida );

            var stock = ui.item.stock;
            // var minimo = 10/100*ui.item.stock;
            $( "#stock" ).html( ui.item.stock);
            $("#stock_add").val(ui.item.stock);

            var pro = ui.item.stock/100;
            var minimo = ui.item.saldo_min/100;
            var color= "";
            if(pro==0){
              color= "red";
              pro=900;
            
            }

            if(pro>0 && 0<minimo){
              color= "red";

            }
            if(pro>minimo && pro<0.7 ){
              color="orange";
            }
            if(pro>0.7 && pro<900){
              color="lime";
            }

            $('#circle').circleProgress({
                value: pro,
                size: 40,
                fill: {

                    gradient: [color]
                }
            });
            // if(ui.item.stock <= 5){
            //   $( "#stock" ).html( ui.item.stock + 'minimo');
            // }else{
            //   $( "#stock" ).html( ui.item.stock + 'maximo');
            // }
            

            $( "#add_unidad_medida" ).val( ui.item.unidad_medida );
            $( "#add_precio_unitario" ).val( ui.item.precio_unitario );
            $( "#add_cantidad" ).val( 1 );


            // para agregar datos de la cabecera a el menu de items
            $( "#add_descuento" ).val($( "#add_descuentoc" ).val());
            $( "#add_recargo" ).val($( "#add_recargoc" ).val());
            $( "#add_ice" ).val($( "#add_icec" ).val());
            $( "#add_exentos" ).val($( "#add_exentosc" ).val());
            // para hacer un select en el menu de items
            var dato_desc = $('input[name="tipo_descuentoc"]:checked').val();
            var dato_recarg = $('input[name="tipo_recargoc"]:checked').val();

            if(dato_desc=='%'){
              dato_desc = 475;
            }else{
              dato_desc = '';
            }

            if(dato_recarg=='%'){
              dato_recarg = 475;
            }else{
              dato_recarg = '';
            }

        
            $('#add_fk_id_formato_dato_descuento option:selected').removeAttr("selected");
            $('#add_fk_id_formato_dato_descuento option[value="'+dato_desc+'"]').attr('selected', 'selected');

            $('#add_fk_id_formato_dato_recargo option:selected').removeAttr("selected");
            $('#add_fk_id_formato_dato_recargo option[value="'+dato_recarg+'"]').attr('selected', 'selected');
            add_calculo_totales();
            
            $('#add_fk_id_formato_dato_recargo').material_select();
            $('#add_fk_id_formato_dato_descuento').material_select();
            
            // $( "#add_descuento" ).val();
            $( "#add_fk_id_formato_dato_descuento" ).val( $( "#fk_id_formato_dato_descuento" ).val());

            // $( "#add_recargo" ).val( $( "#recargo" ).val());
            $( "#add_fk_id_formato_dato_recargo" ).val( $( "#fk_id_formato_dato_recargo" ).val());

            
            // $( "#add_ice" ).val( $( "#ice" ).val());
            $( "#add_fk_id_formato_dato_ice" ).val( $( "#fk_id_formato_dato_ice" ).val());

            $( "#add_excentos" ).val( $( "#excentos" ).val());
            $( "#add_fk_id_formato_dato_excentos" ).val( $( "#fk_id_formato_dato_excentos" ).val());
           
            return false;
          },      
          open: function() {
            $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
          },
          close: function() {
            $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
          }
          });
        
         $( "#add_nit" ).autocomplete({
          source: function( request, response ) {
            console.log(request);
            $.ajax({
              url: "/buscar_cliente/",
              dataType: "json",
              data: {'id':request.term},
              success: function( data ) {
               console.log(data);
               response($.map(data, function (pn) {
                console.log('estoo es stockkkkkkkkkk')
                console.log(pn);
                console.log('uuuuuuuuuuuuuuuuuuuuu')
                return {
                  pk: pn.pk,
                  nit: pn.fields.nit,
                  razonsocial: pn.fields.razonsocial,
                  label: pn.fields.nit+"-"+pn.fields.razonsocial
                };
              }));

             }
           });
          }, 

          focus: function(event, ui) {
            event.preventDefault();
            $(this).val(ui.item.nit);
          },

          minLength: 2,       
          select: function( event, ui ) {
            var fila = new Object();
            fila.pk = ui.item.pk_id_item;
            fila.nit = ui.item.nit;
            fila.razonsocial = ui.item.razonsocial;

            $( "#add_razon" ).focus().val( ui.item.razonsocial );

            return false;
          },      
          open: function() {
            $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
          },
          close: function() {
            $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
          }
          });

          $( "#add_razon" ).autocomplete({
          source: function( request, response ) {
            console.log(request);
            $.ajax({
              url: "/buscar_cliente/",
              dataType: "json",
              data: {'id':request.term},
              success: function( data ) {
               console.log(data);
               response($.map(data, function (pn) {
                console.log('estoo es stockkkkkkkkkk')
                console.log(pn);
                console.log('uuuuuuuuuuuuuuuuuuuuu')
                return {
                  pk: pn.pk,
                  nit: pn.fields.nit,
                  razonsocial: pn.fields.razonsocial,
                  label: pn.fields.razonsocial+"-"+pn.fields.nit
                };
              }));

             }
           });
          }, 

          focus: function(event, ui) {
            event.preventDefault();
            $(this).val(ui.item.razonsocial);
          },

          minLength: 2,       
          select: function( event, ui ) {
            var fila = new Object();
            fila.pk = ui.item.pk_id_item;
            fila.nit = ui.item.nit;
            fila.razonsocial = ui.item.razonsocial;
            
            $( "#add_nit" ).focus().val( ui.item.nit );

            return false;
          },      
          open: function() {
            $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
          },
          close: function() {
            $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
          }
          });

  

  });

var z=dhtmlXComboFromSelect("add_costos");
$('input[name=add_costos]').attr('id', 'add_costos');
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
        add_nit: {
            required: true,
            minlength: 4
        },
        add_razon: {
            required: true,
           
        },
        add_fecha: {
            required: true,
         
        },
        nro_factura: {
          required:true,
        },
        add_autorizacion: {
          required:true,
          minlength: 10,
          number: true
        },
        dias: {
            required: true,
            number: true
        }
    }
});

//====== codigo para desabilitar inputs de almacen =========
// code for disable input is codigo item)===========
function disable() {
  $(".add_disable").attr('disabled', 'disabled');
  $(".add_total").attr('disabled', 'disabled');
  $(".add_scf").attr('disabled', 'disabled');
}

disable();
z.attachEvent("onChange", function(value, text) {
  console.log('changeeeeeeeeeeeeeeeeeeeeee');
    console.log( value ); // or $(this).val()
    if (value == 'A') {
     disable();
     $('#add_buscar_item').removeAttr('disabled');
    }else{
      $('#add_buscar_item').attr('disabled', 'disabled');
       $('.add_disable').removeAttr('disabled');
      $('#add_detalle').val('');
      $( "#add_codigo_item" ).val('');
      $('#add_unidad').val('');
      $('#add_precio_unitario').val('');
      $( "#add_cantidad" ).val('');
      $('#add_total').val('');
      $('#add_sujeto_credito_fiscal').val('');
      
    };
    
});

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



// objeto para guardar productos y factura de la compra
var proceso = new Object();
proceso.producto = new Array();

var table = new Array();
function agregarDetalle(){
  console.log('----datosss array ------------');
      // $("#post_form").prop("target", '_blank');
      // console.log($( "#add_cantidad" ).val());
      // var cant = $( "#add_cantidad" ).val();
      // table.push({'cantidad':cant});
      // console.log(table);
      var d = table;

      var item =  $( "#add_codigo_item" ).val();
      var centroC =  $( "#add_costos" ).val();
      console.log('costosssssssss');
    
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

      console.log(typo_recargo);
      

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

          $( "#add_codigo_item" ).val('');
          $( "#add_detalle" ).val('');
          $( "#add_unidad" ).val('');
          $("#add_precio_unitario").val('');
          $("#add_cantidad").val('');
          $("#add_total").val('');
          $("#add_sujeto_credito_fiscal").val('');
          $("#add_buscar_item").val('');
          $('#add_descuento').val(0);
          $('#add_recargo').val(0);
          $('#add_ice').val(0);
          $('#add_exentos').val(0);

          //======= para validar ==========


          if ($("#encabezado").valid() && proceso.producto.length > 0) {
              $('#save').prop('disabled', false);  
          } else {
              $('#save').prop('disabled', 'disabled');
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
            proceso.nro_factura = $('#add_factura').val();
            proceso.nro_autorizacion = $('#add_autorizacion').val();
            proceso.fecha = $('#add_fecha').val();
            proceso.codigo_control = $('#add_codcontrol').val();
            proceso.descuento = $('#add_descuentoc').val();
            proceso.recargo = $('#add_recargoc').val();
            proceso.ice = $('#add_icec').val();
            proceso.excentos = $('#add_exentosc').val();

            proceso.tipo_descuento = $('input[name="tipo_descuentoc"]:checked').val();
            proceso.tipo_recargo = $('input[name="tipo_recargoc"]:checked').val();

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
          delete proceso['nro_factura'];
          delete proceso['nro_autorizacion']
          delete proceso['codigo_control']
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
          $('#add_factura').val('');
          $('#add_autorizacion').val('');
          $('#add_codcontrol').val('');
          $('#add_fecha').val('');
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
          console.log('procesooooo newwwwww');
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
              url: "/buscar_item/",
              dataType: "json",
              data: {'id':request.term},
              success: function( data ) {
               console.log(data);
               response($.map(data, function (pn) {
                console.log(pn);
                return {
                  pk: pn.pk,
                  codigo_item: pn.fields.codigo_item,
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
          minLength: 2,       
          select: function( event, ui ) {
            var fila = new Object();
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
              url: "/buscar_proveedor/",
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
                  razon_social: pn.fields.razon_social,
                  label: pn.fields.nit+"-"+pn.fields.razon_social
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
            fila.razon_social = ui.item.razon_social;

            $( "#add_razon" ).focus().val( ui.item.razon_social );

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
              url: "/buscar_proveedor/",
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
                  razon_social: pn.fields.razon_social,
                  label: pn.fields.razon_social+"-"+pn.fields.nit
                };
              }));

             }
           });
          }, 

          focus: function(event, ui) {
            event.preventDefault();
            $(this).val(ui.item.razon_social);
          },

          minLength: 2,       
          select: function( event, ui ) {
            var fila = new Object();
            fila.pk = ui.item.pk_id_item;
            fila.nit = ui.item.nit;
            fila.razon_social = ui.item.razon_social;
            
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

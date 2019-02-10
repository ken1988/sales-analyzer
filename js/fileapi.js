// -------------------------------------------------------------------
//  fileapi.js
//
//                  Jun/30/2017
// -------------------------------------------------------------------
jQuery (function ()
{
    var file = jQuery('#sales_csv')[0]
    file.onchange = function ()
    {
    const fileList = file.files
    var reader = new FileReader()
    reader.readAsText(fileList[0],"Shift-jis")

    reader.onload = function ()
        {
        jQuery('#preview').text(reader.result)
        }
    }
})
// -------------------------------------------------------------------
/**
 * Created with PyCharm.
 * User: robertv
 * Date: 5/5/13
 * Time: 10:24 AM
 * To change this template use File | Settings | File Templates.
 */

/**
<script type="text/javascript">
var client = new XMLHttpRequest();
client.open("GET", "http://zip.elevenbasetwo.com?zip=48867", true);
client.onreadystatechange = function() {
if(client.readyState == 4) {
alert(client.responseText);
};
};

client.send();
</script>

Result:

{"country": "US", "state": "MI", "city": "OWOSSO"}
 **/

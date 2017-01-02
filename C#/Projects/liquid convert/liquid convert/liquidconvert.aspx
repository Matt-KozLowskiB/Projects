<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="liquidconvert.aspx.cs" Inherits="liquid_convert.liquidconvert" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Gallons<>Liters</title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        <p>Liters:  <input data-bind="value: lit" /> =
        <b data-bind="text: gal1" ></b> Gallon(s)</p>
        <p>Gallons:  <input data-bind="value: gal" /> =  
        <b data-bind="text: lit1"></b> Liter(s) </p>        
    </div>
    </form>
    <script src="scripts/knockout-3.4.0.js"></script>
    <script type ="text/javascript">

        function viewmod() {
           this.gal = ko.observable(1);
           this.lit = ko.observable(3.78);
           this.gal1 = ko.computed(function () {
               return this.lit()/3.78}, this);
           this.lit1 = ko.computed(function () {
               return this.gal()*3.78}, this);
        }

        ko.applyBindings(viewmod());

    </script>
</body>
</html>

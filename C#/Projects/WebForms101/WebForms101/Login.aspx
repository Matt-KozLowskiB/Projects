<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Login.aspx.cs" Inherits="WebForms101.Login" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        #form1 {
            width: 409px;
            height: 390px;
            margin-top: 12px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <asp:Label ID="Label1" runat="server" Text="First Name:"></asp:Label>
        <asp:TextBox ID="txtFirst" runat="server" BorderColor="Lime" BorderStyle="Ridge" ForeColor="#00CCFF" Height="16px" OnTextChanged="TextBox1_TextChanged" style="margin-left: 7px; margin-top: 0px"></asp:TextBox>
        <br />
        <br />
        <asp:Label ID="Label2" runat="server" Text="Last Name:"></asp:Label>
        <asp:TextBox ID="txtLast" runat="server" BorderColor="#00CCFF" BorderStyle="Groove" ForeColor="Lime" Height="16px" OnTextChanged="TextBox2_TextChanged" style="margin-left: 8px; margin-top: 0px; margin-bottom: 0px"></asp:TextBox>
        <br />
        <br />
        <asp:Button ID="btnSubmit" runat="server" Font-Italic="True" ForeColor="#0099CC" OnClick="btnSubmit_Click1" Text="Login" />
        <br />
        <br />
        <asp:Label ID="lblName" runat="server" BackColor="White" BorderStyle="Inset" Font-Bold="False" Font-Size="Small" ForeColor="Red" ViewStateMode="Enabled"></asp:Label>
    </form>
</body>
</html>

namespace TemplateEngine.Tests;
 
public class TemplateEngineTests
{
    [SetUp]
    public void Setup() {}
 
    [TestCase( "Tracey" )]
    [TestCase( "Kat" )]
    [TestCase( "Rick" )]
    public void ShouldEvaluateOneVariable( string value )
    {
        //Arrange
        TemplateEngine templateEngine = new();
        templateEngine.SetTemplate( "Hello {name}" );
        templateEngine.SetVariable( "name", value );
 
        //Act
        string result = templateEngine.Evaluate();
 
        //Assert
        Assert.That( result, Is.EqualTo( "Hello " + value ) );
    }
 
    [TestCase( "Tracey", "XYZ" )]
    [TestCase( "Kat", "XYZ" )]
    [TestCase( "Rick", "XYZ" )]
    public void ShouldEvaluateOneVariable( string name, string company )
    {
        //Arrange
        TemplateEngine templateEngine = new();
        templateEngine.SetTemplate( "Hello, {name} {company}" );
        templateEngine.SetVariable( "name", name );
        templateEngine.SetVariable( "company", company );
 
        //Act
        string result = templateEngine.Evaluate();
 
        //Assert
        Assert.That( result, Is.EqualTo( "Hello, " + name + " " + company ) );
    }
}

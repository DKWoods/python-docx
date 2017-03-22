Feature: Add picture to a run
  In order to place an inline picture at an arbitrary place in a document
  As a developer using python-docx
  I need a way to add a picture to a run


  Scenario: Add a picture to a body paragraph run
    Given a run
     When I add a picture to the run
     Then the picture appears at the end of the run
      And the document contains the inline picture


  Scenario Outline: Add a picture to a run in a table cell
    Given a run inside a table cell retrieved from <cell-source>
     When I add a picture to the run
     Then the picture appears at the end of the run
      And the document contains the inline picture

    Examples: Table cell sources
      | cell-source        |
      | Table.cell         |
      | Table.row.cells    |
      | Table.column.cells |


  Scenario: A run without a picture
    Given a run
     Then has_picture is False
     

  Scenario: A run with a picture
    Given a run
     When I add a picture to the run
     Then has_picture is True


  Scenario: A picture knows its data
    Given a run
      When I add a picture to the run
      Then the picture's rId is rId9    
       And the picture's filename is monty-truth.png
       And the picture's extension is png
       And the picture's type is image/png       
       And the picture's size is 1905000, 2717800
       And the picture's image_data size is 64276
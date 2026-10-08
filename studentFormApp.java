import javax.swing.*;
import java.awt.*;
import java.util.List;
public class StudentFormApp extends Jframe{
private JTexField nameField=new JTextField(15);
private JComboBox<String>courseComboBox=new
JComboBoxX<>(new String[]{"Computer Science","Information Technology","Business","Mechanical"});
private Jlist<String> clubsList=new JList<>(new String[]{"Coding Club","Drama Club","Sports Club","Music Band"});
public StudentFormApp()
{
setTitle("Student Form");
setSize(350,300);
setDefaultCloseOperation(Exit_ON__CLOSE);
setLocationRelativeTo(null);
setLayout(new gridLayout(4,2,10,10));
add(new JLabel("Full Name:"));
add(nameField);
add(new JLabel("select course:"));
add(courseComboBox);
add(new Jlabel("select Clubs:"));
JButton submitButton=new JButton("Submit");
add(new JLabel(""));
add(submitButton);
submitButton.addActionListener(e->
{
String name=nameField.getText().trim();
if(name.isEmpty()){
JOptionpane.showMessageDialog(this,"Please enter a name.","Error",JOptionPane.ERROR_MESSAGE);
return;
}
List<String>clubs=clubsList.getSelectedValuesList();
string clubSummery=clubs.isEmpty()?"None":String.join(",",clubs);
string msg=String.format("Registered!\nName:%s\nCourse:%s\nClubs:%s",name,courseComboBox.getSelectedItem(),clubsSummery);
JoptionPane.showMessageDialog(this,msg,"Success",JOptionPane.INFORMATION_MESSAGE);
});
}
public static void main(String[] args)
{
SwingUtilities.invokelater(()-> new
StudentFormApp()setVisible(true);
}
}

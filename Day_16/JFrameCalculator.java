// Fix calcultor to handle math expressions...
// Getting error when trying to evaluate expressions like 2+2*2

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class JFrameCalculator {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Calculator");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(300, 400);
            frame.setLayout(new BorderLayout());

            JPanel displayPanel = new JPanel();
            JTextField displayField = new JTextField(10);
            displayField.setEditable(false);
            displayPanel.add(displayField);

            JPanel buttonPanel = new JPanel();
            buttonPanel.setLayout(new GridLayout(5, 4)); // Increased rows for the Clear button

            String[] buttonLabels = {
                    "7", "8", "9", "/",
                    "4", "5", "6", "*",
                    "1", "2", "3", "-",
                    "0", ".", "=", "+",
                    "C" // Clear button
            };

            for (String label : buttonLabels) {
                JButton button = new JButton(label);
                button.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        String text = displayField.getText();
                        if (label.equals("=")) {
                            try {
                                double result = evaluateExpression(text);
                                displayField.setText(Double.toString(result));
                            } catch (Exception ex) {
                                displayField.setText("Error");
                            }
                        } else if (label.equals("C")) {
                            displayField.setText(""); // Clear the display
                        } else {
                            displayField.setText(text + label);
                        }
                    }
                });
                buttonPanel.add(button);
            }

            frame.add(displayPanel, BorderLayout.NORTH);
            frame.add(buttonPanel, BorderLayout.CENTER);

            frame.setVisible(true);
        });
    }

    private static double evaluateExpression(String expression) {
        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("js");
        try {
            Object result = engine.eval(expression);
            if (result instanceof Number) {
                return ((Number) result).doubleValue();
            } else {
                throw new RuntimeException("Invalid expression");
            }
        } catch (ScriptException e) {
            throw new RuntimeException("Invalid expression");
        }
    }
}

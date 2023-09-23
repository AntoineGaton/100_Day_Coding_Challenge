import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ShapeGeneratorApp {
    public static void main(String[] args) {
        // Create the main JFrame window
        JFrame frame = new JFrame("Shape Generator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Close the application when the window is closed
        frame.setSize(400, 400); // Set the size of the window
        frame.setLayout(new BorderLayout()); // Use BorderLayout to organize components

        // Create a JPanel to hold buttons in a 2x2 grid
        JPanel buttonPanel = new JPanel(new GridLayout(2, 2));

        // Create an array of JPanels to hold shapes (using CardLayout to switch between buttons and shapes)
        JPanel[] shapePanels = new JPanel[4];
        for (int i = 0; i < 4; i++) {
            shapePanels[i] = new JPanel(new CardLayout());

            // Create a button for each shape
            JButton button = new JButton("Create Shape " + (i + 1));
            int finalI = i;
            button.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    createShape(shapePanels[finalI], finalI + 1);
                }
            });

            // Add the button to the button panel
            shapePanels[i].add(button, "button");
            buttonPanel.add(shapePanels[i]);
        }

        // Create a "Reset" button
        JButton resetButton = new JButton("Reset");
        resetButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Show the original buttons again
                for (JPanel panel : shapePanels) {
                    CardLayout cardLayout = (CardLayout) panel.getLayout();
                    cardLayout.show(panel, "button");
                }
            }
        });

        // Add the button panel and the Reset button to the main frame
        frame.add(buttonPanel, BorderLayout.CENTER);
        frame.add(resetButton, BorderLayout.SOUTH);

        frame.setLocationRelativeTo(null); // Center the frame on the screen
        frame.setVisible(true); // Make the frame visible
    }

    // Method to create and display a shape in a JPanel
    private static void createShape(JPanel panel, int shapeType) {
        CardLayout cardLayout = (CardLayout) panel.getLayout(); // Get the CardLayout of the panel

        JComponent shapeComponent;
        switch (shapeType) {
            case 1:
                shapeComponent = new RectangleComponent();
                break;
            case 2:
                shapeComponent = new CircleComponent();
                break;
            case 3:
                shapeComponent = new TriangleComponent();
                break;
            case 4:
                shapeComponent = new StarComponent();
                break;
            default:
                shapeComponent = new JPanel(); // Default empty panel if shapeType is invalid
                break;
        }

        panel.add(shapeComponent, "shape"); // Add the shape with a "shape" identifier
        cardLayout.show(panel, "shape"); // Switch to the shape view
    }
}

// Custom JComponent classes for different shapes (same as before)

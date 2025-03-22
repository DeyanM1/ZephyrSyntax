import * as vscode from "vscode";

export function activate(context: vscode.ExtensionContext) {
  // Create a status bar item that we can now manage
  const myButton = vscode.window.createStatusBarItem(
    vscode.StatusBarAlignment.Right,
    100
  );
  myButton.text = "$(zap) Click Me";
  myButton.tooltip = "Do something cool";
  myButton.command = "myExtension.doAction";
  myButton.show();

  // Register the command invoked when the button is clicked
  const disposable = vscode.commands.registerCommand(
    "myExtension.doAction",
    () => {
      vscode.window.showInformationMessage("Button clicked!");
    }
  );
  context.subscriptions.push(myButton, disposable);
}

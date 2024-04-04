<script>
    let textContent = ""; // This will hold the text entered by the user
    
    function format(command, value = null) {
      document.execCommand(command, false, value);
    }
    function changeLanguage(lang) {
    selectedLanguage = lang;
  }
  </script>
  
  <div class="flex flex-col items-center space-y-2">
    <div class="flex space-x-2 justify-center">
      <!-- Existing Buttons -->
      <button on:click={() => format('bold')} class="button" title="Bold">B</button>
      <button on:click={() => format('italic')} class="button" title="Italic">I</button>
      <button on:click={() => format('underline')} class="button" title="Underline">U</button>
      <input type="color" on:input="{(e) => format('foreColor', e.target.value)}" class="color-picker" title="Text Color" />
      <select on:change="{(e) => format('fontSize', e.target.value)}" class="button" title="Font Size">
        <option value="1">Small</option>
        <option value="3" selected>Normal</option>
        <option value="5">Large</option>
        <option value="7">Huge</option>
      </select>
  
      <!-- Font Family Dropdown -->
      <select on:change="{(e) => format('fontName', e.target.value)}" class="button" title="Font Family">
        <option value="Arial">Arial</option>
        <option value="'Courier New', Courier, monospace">Courier New</option>
        <option value="Georgia">Georgia</option>
        <option value="Tahoma">Tahoma</option>
        <option value="'Times New Roman', Times, serif">Times New Roman</option>
        <option value="Verdana">Verdana</option>
      </select>

      <select on:change="{(e) => changeLanguage(e.target.value)}" class="button" title="Language">
        <option value="en">English</option>
        <option value="fr">Français</option>
        <option value="es">Español</option>
        <option value="de">Deutsch</option>
        <option value="ar">العربية</option>
        <!-- Add more languages as needed -->
      </select>
    </div>
  
    <div contenteditable="true" bind:textContent class="editor" role="textbox" aria-multiline="true">
      {textContent}
    </div>
  </div>
  
  <style>
    .button {
      background-color: #065f46;
      color: #ffffff;
      font-weight: bold;
      padding: 4px 8px;
      font-size: 0.875rem;
      border-radius: 0.25rem;
      cursor: pointer;
      transition: background-color 300ms ease-in-out;
    }
  
    .button:hover {
      background-color: #0b4a32;
    }
  
    .color-picker {
      height: 2rem;
      width: 2rem;
      padding: 0;
      border: none;
      cursor: pointer;
    }
  
    .editor {
      border: 2px solid #cccccc;
      padding: 10px;
      min-height: 400px;
      width: 600px;
      font-family: 'Courier New', Courier, monospace;
      white-space: pre-wrap;
      overflow-wrap: break-word;
      position: relative;
      z-index: 50;
      background-color: rgba(255, 255, 255, 0.8) !important;
    }
  </style>
  
<!-- The component where you want to include the Quill editor -->
<script>
  import MyWorks from '$lib/MyWorks.svelte';
  import TextEditor from '$lib/TextEditor.svelte'
  </script>

<MyWorks />

<div class="flex flex-col items-center justify-center h-screen bg-cover bg-center" style="background-image: url('fairy.png');">
  <TextEditor /> <!-- Include the RichTextEditor component -->
  <button class="bg-green-700 text-white font-bold py-2 px-4 rounded hover:bg-green-900 transition duration-300">Save</button>
</div>

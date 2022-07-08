<p>Not long ago a young Christmas elf asked you to implement a function that creates Christmas trees made of asterisks (<code>'*'</code>) similar to the one below:</p>
<pre><code>    *    
    *    
   ***   
  *****  
 ******* 
*********
   ***   
</code></pre>
<p>Unfortunately because of the extreme coldness the <code>tree</code> that you sent over was corrupted: although its lines are given in the correct order, but are not aligned properly. Now your task is to fix the given <code>tree</code> by centering the asterisks in each line.</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>tree = [
  "      *  ", 
  "    *    ", 
  "***      ", 
  "    *****", 
  "  *******", 
  "*********", 
  " ***     "
]
</code></pre>
<p>the output should be</p>
<pre><code>solution(tree) = [
  "    *    ", 
  "    *    ", 
  "   ***   ", 
  "  *****  ", 
  " ******* ", 
  "*********", 
  "   ***   "
]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string tree</strong></p>
<p>A list representing a tree, where all strings have the same odd length and have the format <code>"&lt; &gt;&lt;*&gt;&lt; &gt;"</code>, where <code>&lt; &gt;</code> denotes some (possibly none) whitespace characters, and <code>&lt;*&gt;</code> denotes an odd number of asterisk.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ tree.length ≤ 31</code>,<br />
<code>1 ≤ tree[0].length ≤ 21</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>A fixed <code>tree</code>, with asterisks centered in each line.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

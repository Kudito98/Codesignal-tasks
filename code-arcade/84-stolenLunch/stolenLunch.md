<p>When you recently visited your little nephew, he told you a sad story: there's a bully at school who steals his lunch every day, and locks it away in his locker. He also leaves a <code>note</code> with a strange, coded message. Your nephew gave you one of the notes in hope that you can decipher it for him. And you did: it looks like all the digits in it are replaced with letters and vice versa. Digit <code>0</code> is replaced with <code>'a'</code>, <code>1</code> is replaced with <code>'b'</code> and so on, with digit <code>9</code> replaced by <code>'j'</code>.</p>
<p>The <code>note</code> is different every day, so you decide to write a function that will decipher it for your nephew on an ongoing basis.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>note = "you'll n4v4r 6u4ss 8t: cdja"</code>, the output should be<br />
<code>solution(note) = "you'll never guess it: 2390"</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string note</strong></p>
<p>A string consisting of lowercase English letters, digits, punctuation marks and whitespace characters (<code>' '</code>).</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ note.length ≤ 500</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The deciphered <code>note</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

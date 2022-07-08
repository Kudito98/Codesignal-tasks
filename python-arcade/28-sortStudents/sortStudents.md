<p>You are given a list of <code>students</code> who want to apply to the internship at CodeSignal. For the <code>i<sup>th</sup></code> student you know their full name <code>students[i]</code>, which can consist of up to <code>5</code> words (where a word is a set of consecutive letters). It is guaranteed that the surname is always the last name of student's full name.</p>
<p>Your task is to sort the students <a href="keyword://lexicographical-order-for-strings" target="_blank">lexicographically</a> by their surnames. If two students happen to have the same surname, their order in the result should be the same as in the original list.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>students = ["John Smith", "Jacky Mon Simonoff", 
            "Lucy Smith", "Angela Zimonova"]
</code></pre>
<p>the output should be</p>
<pre><code>solution(students) = ["Jacky Mon Simonoff", "John Smith", 
                          "Lucy Smith", "Angela Zimonova"]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string students</strong></p>
<p>Array of students, where each student is given by their full name consisting of at most <code>5</code> words. For each <code>i</code> <code>students[i]</code> consists of English letters and whitespace (<code>' '</code>) characters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ students.length ≤ 30</code>,<br />
<code>1 ≤ students[i].length ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>Array of <code>students</code> sorted as described above.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>

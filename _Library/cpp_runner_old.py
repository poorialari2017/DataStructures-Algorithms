# cpp_runner.py
import subprocess
import sys
import os
import tempfile


class CppRunner:
    def __init__(self):
        self.compilers = ['g++', 'gcc', 'clang++', 'c++']
        self.found_compiler = self._find_compiler()

    def _find_compiler(self):
        """Find available C++ compiler"""
        for compiler in self.compilers:
            try:
                result = subprocess.run([compiler, '--version'],
                                        capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    print(f"✅ Found compiler: {compiler}")
                    return compiler
            except:
                continue
        return None

    def run_cpp_code(self, cpp_code, output_filename="output"):
        """Compile and run C++ code"""
        if not self.found_compiler:
            print("❌ No C++ compiler found!")
            return False

        try:
            # Create temporary file
            with open(f'{output_filename}.cpp', 'w', encoding='utf-8') as f:
                f.write(cpp_code)

            print("📝 C++ file created")

            # Compile
            print("🔨 Compiling C++ code...")
            compile_cmd = [self.found_compiler, f'{output_filename}.cpp', '-o', output_filename]
            if sys.platform == 'win32':
                compile_cmd[-1] = f'{output_filename}.exe'

            compile_result = subprocess.run(compile_cmd, capture_output=True, text=True)

            if compile_result.returncode == 0:
                print("✅ Compilation successful!")

                # Run
                print("🚀 Running C++ program...")
                run_cmd = [f'./{output_filename}']
                if sys.platform == 'win32':
                    run_cmd = [f'{output_filename}.exe']

                run_result = subprocess.run(run_cmd, capture_output=True, text=True)

                print("=" * 50)
                print("C++ PROGRAM OUTPUT:")
                print("=" * 50)
                print(run_result.stdout)
                if run_result.stderr:
                    print("STDERR:", run_result.stderr)
                print("=" * 50)

                return True
            else:
                print("❌ Compilation failed!")
                print("Error:", compile_result.stderr)
                return False

        except Exception as e:
            print(f"❌ Error: {e}")
            return False
        finally:
            # Cleanup
            self._cleanup(output_filename)

    def _cleanup(self, filename):
        """Clean up temporary files"""
        files_to_remove = [
            f'{filename}.cpp',
            f'{filename}',
            f'{filename}.exe'
        ]

        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)
                print(f"🧹 Cleaned up: {file}")


# Create global instance
cpp_runner = CppRunner()


# Simple function for quick usage
def run_cpp(cpp_code, output_name="output"):
    """Quick function to run C++ code"""
    return cpp_runner.run_cpp_code(cpp_code, output_name)
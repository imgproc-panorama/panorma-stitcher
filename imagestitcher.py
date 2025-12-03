import argparse
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class ImageStitcher:
    """Class to stitch multiple images into a panorama."""
    def __init__(self):
        # Initialize the stitcher object from OpenCV
        self.stitcher = cv.Stitcher_create()
        self.images = []

    def set_images(self, images: list[np.ndarray]) -> None:
        """Set the images to be stitched.
        
        Args:
            images (list of np.ndarray): List of images to stitch.
        """
        self.images = images

    def get_images(self) -> list[np.ndarray]:
        """Get the images to be stitched.
        
        Returns:
            list of np.ndarray: List of images to stitch.
        """
        return self.images

    def show_images(self) -> None:
        """Display the images to be stitched."""
        plt.figure(figsize=(15, 5))
        for idx, img in enumerate(self.images):
            plt.subplot(1, len(self.images), idx + 1)
            plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
            plt.title(f'Image {idx+1}')
            plt.axis('off')
        plt.show()

    def stitch(self) -> np.ndarray:
        """Stitch the images together.

        Returns:
            np.ndarray: The stitched panorama image.
        """
        status, panorama = self.stitcher.stitch(self.images)
        if status != cv.Stitcher_OK:
            raise RuntimeError("Error during stitching: {}".format(status))
        return panorama

    def get_panorama(self) -> np.ndarray:
        """Get the stitched panorama image.
        
        Returns:
            np.ndarray: The stitched panorama image.
        """
        return self.stitch()

    def show_result(self, panorama: np.ndarray) -> None:
        """Display the stitched panorama image.
        
        Args:
            panorama (np.ndarray): The stitched panorama image.
        """
        plt.figure(figsize=(10, 5))
        plt.imshow(cv.cvtColor(panorama, cv.COLOR_BGR2RGB))
        plt.title('Stitched Panorama')
        plt.axis('off')
        plt.show()

def main(image_paths: list[str], output: str = 'stitched_panorama.jpg') -> None:
    """Stitch images into a panorama and save the result.

    Args:
        image_paths: List of paths to input images.
        output: Path to save the stitched panorama.
    """
    # Load images
    images = [cv.imread(path) for path in image_paths]

    # Check that images loaded correctly
    for i, (path, img) in enumerate(zip(image_paths, images)):
        if img is None:
            print(f"[ERROR] Failed to load image: {path}")
            return

    # Create an ImageStitcher instance
    stitcher = ImageStitcher()
    stitcher.set_images(images)

    try:
        panorama = stitcher.stitch()
    except RuntimeError as e:
        print(f"[ERROR] {e}")
        return

    # Save the result
    cv.imwrite(output, panorama)
    print(f"[OK] Stitched panorama saved to {output}")


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Stitch multiple images into a panorama.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s img1.jpg img2.jpg img3.jpg
  %(prog)s img1.jpg img2.jpg -o panorama.jpg
  %(prog)s images/*.jpg --output result.png
        """
    )
    parser.add_argument(
        "images",
        nargs="+",
        help="Input image files to stitch (minimum 2)"
    )
    parser.add_argument(
        "-o", "--output",
        default="stitched_panorama.jpg",
        help="Output file path (default: stitched_panorama.jpg)"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args.images, args.output)